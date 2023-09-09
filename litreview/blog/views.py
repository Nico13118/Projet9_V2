from django.shortcuts import render, redirect, get_object_or_404
from . import forms, models
from django.contrib.auth.decorators import login_required
from django.db.models import CharField, Value
from itertools import chain


@login_required
def home(request):
    reviews = models.Review.objects.all()
    tickets_reviews = models.Review.objects.all()

    return render(request, 'blog/flow.html', context={'tickets_reviews': tickets_reviews})


@login_required
def flow(request):
    tickets = models.Ticket.objects.all()
    reviews = models.Review.objects.all()
    my_following = request.user.following.all()
    user_connected = str(request.user)

    for ticket in tickets:

        if ticket.response == '0':
            if ticket.user.username == user_connected:
                ticket.entry_type = "Ticket_Not_Response"
            if ticket.user.username != user_connected:
                for follow in my_following:
                    follow = str(follow)
                    if ticket.user.username == follow:
                        ticket.entry_type = "Ticket_Not_Response"
        if ticket.response == '1':
            if ticket.user.username == user_connected:
                ticket.entry_type = "Ticket_Response"
            for follow in my_following:
                follow = str(follow)
                if ticket.user.username == follow:
                    ticket.content_type = "Ticket_Response"

        if ticket.response == '1':
            for review in reviews:
                if review.ticket_id == ticket.id:
                    if ticket.user.username == user_connected:
                        review.entry_type = "Review"
                        ticket.entry_type = "Ticket_Response"

                    for follow in my_following:
                        follow = str(follow)
                        if ticket.user.username == follow:
                            review.entry_type = "Review"
                            ticket.entry_type = "Ticket_Response"

                        if review.user.username == follow:
                            review.entry_type = "Review"
                            ticket.entry_type = "Ticket_Response"

    entries = sorted(chain(tickets, reviews), key=lambda x: x.date_created, reverse=True)
    return render(request, 'blog/flow.html', context={'entries': entries})


@login_required
def posts(request):
    tickets = models.Ticket.objects.all()
    reviews = models.Review.objects.all()
    user_connected = str(request.user)

    for ticket in tickets:
        if ticket.user.username == user_connected:
            ticket.entry_type = "Ticket_Response"
            for review in reviews:
                if review.user.username == user_connected:
                    if review.ticket_id == ticket.id:
                        if review.user.username == user_connected:
                            review.entry_type = "Review"
                            ticket.entry_type = "Ticket_Response"
                if ticket.user.username == user_connected:
                    review.entry_type = "Review"
                    ticket.entry_type = "Ticket_Response"

    entries = sorted(chain(tickets, reviews), key=lambda x: x.date_created, reverse=True)
    return render(request, 'blog/posts.html', context={'entries': entries})


@login_required
def create_ticket(request):
    ticket_form = forms.TicketForm()
    photo_form = forms.PhotoForm()
    if request.method == 'POST':
        ticket_form = forms.TicketForm(request.POST)
        photo_form = forms.PhotoForm(request.POST, request.FILES)
        if all([ticket_form.is_valid(), photo_form.is_valid()]):
            photo = photo_form.save(commit=False)
            photo.uploader = request.user
            photo.save()
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.photo = photo
            ticket.save()
            return redirect('flow')
    context1 = {
        'ticket_form': ticket_form,
        'photo_form': photo_form,
    }
    return render(request, 'blog/create_ticket.html', context=context1)


@login_required
def review_not_in_response(request):
    ticket_form = forms.TicketForm()
    review_form = forms.ReviewForm()
    photo_form = forms.PhotoForm()
    if request.method == 'POST':
        ticket_form = forms.TicketForm(request.POST)
        review_form = forms.ReviewForm(request.POST)
        photo_form = forms.PhotoForm(request.POST, request.FILES)
        if all([ticket_form.is_valid(), review_form.is_valid(), photo_form.is_valid()]):
            photo = photo_form.save(commit=False)
            photo.uploader = request.user
            photo.save()
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.photo = photo
            ticket.response = 1
            ticket.save()
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket_id = ticket.id
            selected_rating = request.POST.getlist('rating')
            if selected_rating:
                review.rating = int(selected_rating[0])
                review.save()
                return redirect('flow')
            else:
                review.rating = 0
                review.save()
                return redirect('flow')
    context2 = {
        'review_form': review_form,
        'photo_form': photo_form,
        'ticket_form': ticket_form,
    }
    return render(request, 'blog/review_not_in_response.html', context=context2)


@login_required
def review_in_response(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    edit_ticket_form = forms.TicketForm(instance=ticket)
    review_form = forms.ReviewForm()
    if request.method == 'POST':
        edit_ticket_form = forms.TicketForm(request.POST, instance=ticket)
        review_form = forms.ReviewForm(request.POST)
        ticket.response = 1
        edit_ticket_form.save()
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            selected_rating = request.POST.getlist('rating')
            if selected_rating:
                review.rating = int(selected_rating[0])
                review.save()
                return redirect('flow')
            else:
                review.rating = 0
                review.save()
                return redirect('flow')
    context3 = {
        'review_form': review_form,
        'ticket': ticket,
        'edit_ticket_form': edit_ticket_form,
    }
    return render(request, 'blog/review_in_response.html', context=context3)

@login_required
def edit_review_in_response(request, review_id):
    review = get_object_or_404(models.Review, id=review_id)
    edit_review_form = forms.ReviewForm(instance=review)
    tickets = models.Ticket.objects.all()
    for ticket in tickets:
        if ticket.id == review.ticket_id:
            ticket_id = ticket.id
            print("ticket id :", ticket_id)
            print("review_id :", review_id)
            ticket = get_object_or_404(models.Ticket, id=ticket_id)
            edit_ticket_form = forms.TicketForm(instance=ticket)
            if request.method == 'POST':
                edit_review_form = forms.ReviewForm(request.POST, instance=review)
                edit_ticket_form = forms.TicketForm(request.POST, instance=ticket)
                edit_ticket_form.save()
                if edit_review_form.is_valid():
                    review = edit_review_form.save(commit=False)
                    review.user = request.user
                    review.ticket = ticket
                    select_rating = request.POST.getlist('rating')
                    if select_rating:
                        review.rating = int(select_rating[0])
                        review.save()
                        return redirect('posts')
                    else:
                        review.rating = 0
                        review.save()
                        return redirect('posts')
            context4 = {
                'edit_review_form': edit_review_form,
                'edit_ticket_form': edit_ticket_form,
                'ticket': ticket,
                'review': review,
            }
            return render(request, 'blog/edit_review_in_response.html', context=context4)


# blog\views.py
@login_required
def follow_users(request):
    # form  = Récupère la liste des utilisateurs inscrits
    form = forms.FollowUsersForm(instance=request.user)

    # del_following = Récupère la liste de mes abonnements depuis la classe DeleteFollowingForm
    del_following = forms.DeleteFollowingForm(user=request.user)

    # my_following = Récupère la liste de mes abonnements
    my_following = request.user.following.all()

    # my_followers = Récupère la liste des personnes qui me suivent
    my_followers = request.user.follower.all()

    # fonctionnalité qui permet d'exclure de la liste, l'utilisateur connecté
    form.fields['following'].queryset = form.fields['following'].queryset.exclude(
        username=request.user.username)

    # fonctionnalité qui permet de ne pas afficher dans la 'Liste des utilisateurs' mes abonnements
    form.fields['following'].queryset = form.fields['following'].queryset.exclude(
        id__in=my_following)

    if request.method == 'POST':
        if 'form' in request.POST:
            form = forms.FollowUsersForm(request.POST, instance=request.user)
            if form.is_valid():
                user = form.save(commit=False)
                # following_user > Récupère l'utilisateur qui a été selectionné dans la liste
                following_user = form.cleaned_data.get('following')
                user.save()
                user.following.add(*following_user)
                return redirect('subscriptions')

        if 'del_following' in request.POST:
            del_following = forms.DeleteFollowingForm(request.POST, user=request.user)
            if del_following.is_valid():
                following_to_delete = del_following.cleaned_data['following_to_delete']
                request.user.following.remove(following_to_delete)
                return redirect('subscriptions')

    return render(request, 'blog/subscriptions.html', context={'form': form,
                                                               'my_followers': my_followers,
                                                               'del_following': del_following})
