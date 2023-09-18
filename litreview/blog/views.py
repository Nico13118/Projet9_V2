from django.shortcuts import render, redirect, get_object_or_404
from . import forms, models
from django.contrib.auth.decorators import login_required
from itertools import chain


@login_required
def flow(request):
    tickets_user = models.Ticket.objects.filter(user=request.user)
    tickets_user_follow = models.Ticket.objects.filter(user__in=request.user.following.all())
    reviews_user = models.Review.objects.filter(user=request.user)
    reviews_user_follow = models.Review.objects.filter(user__in=request.user.following.all())
    reviews_follower = models.Review.objects.filter(user__in=request.user.follower.all())

    for ticket_user_follow in tickets_user_follow:

        """ Affiche le ticket de mes following avec réponse """
        if ticket_user_follow.response == '1':
            ticket_user_follow.entry_type = "Ticket_Response"

            for review_user in reviews_user:

                """Affiche la review de l'utilisateur connecté et le ticket des mes following """
                if review_user.ticket_id == ticket_user_follow.id:
                    review_user.entry_type = "Review"

            for review_user_follow in reviews_user_follow:
                for ticket_user in tickets_user:

                    """ Affiche la review et ticket de mes following """
                    if review_user_follow.ticket_id == ticket_user_follow.id:
                        review_user_follow.entry_type = "Review"

                    """Affiche la review de mes following et le ticket de l'utilisateur connecté """
                    if review_user_follow.ticket_id == ticket_user.id:
                        review_user_follow.entry_type = "Review"

        """ Affiche le ticket (sans réponse) de mes following """
        if ticket_user_follow.response == '0':
            ticket_user_follow.entry_type = "Ticket_Not_Response"

    for ticket_user in tickets_user:

        """ Affiche le ticket (sans réponse) de l'utilisateur connecté """
        if ticket_user.response == '0':
            ticket_user.entry_type = "Ticket_Not_Response"

        """ Affiche le ticket (avec réponse) de l'utilisateur connecté """
        if ticket_user.response == '1':
            ticket_user.entry_type = "Ticket_Response"
            for review_user in reviews_user:

                """ Affiche la review et ticket de l'utilisateur connecté """
                if review_user.ticket_id == ticket_user.id:
                    review_user.entry_type = "Review"

            for review_follower in reviews_follower:
                """ Affiche la review de mes followers du ticket de l'utilisateur connecté"""
                if review_follower.ticket_id == ticket_user.id:
                    review_follower.entry_type = "Review"

    entries = sorted(chain(tickets_user, tickets_user_follow, reviews_user, reviews_user_follow, reviews_follower),
                     key=lambda x: x.date_created, reverse=True)
    return render(request, 'blog/flow.html', context={'entries': entries})


@login_required
def posts(request):
    tickets_user = models.Ticket.objects.filter(user=request.user)
    tickets_user_follow = models.Ticket.objects.filter(user__in=request.user.following.all())
    reviews_user = models.Review.objects.filter(user=request.user)
    reviews_user_follow = models.Review.objects.filter(user__in=request.user.following.all())

    for ticket_user_follow in tickets_user_follow:
        if ticket_user_follow.response == '1':
            for review_user in reviews_user:

                """Affiche la review de l'utilisateur connecté et le ticket de mes following"""
                if review_user.ticket_id == ticket_user_follow.id:
                    review_user.entry_type = "Review_User_Ticket_Follow"

            for review_user_follow in reviews_user_follow:
                for ticket_user in tickets_user:

                    """Affiche la review de mes following et le ticket de l'utilisateur connecté"""
                    if review_user_follow.ticket_id == ticket_user.id:
                        review_user_follow.entry_type = "Review_Follow_Ticket_User"

    for ticket_user in tickets_user:

        """ Affiche le ticket ( avec réponse ) de l'utilisateur connecté """
        if ticket_user.response == '1':
            ticket_user.entry_type = "Ticket_User_Response"
            for review_user in reviews_user:

                """ Affiche la review et ticket de l'utilisateur connecté """
                if review_user.ticket_id == ticket_user.id:
                    review_user.entry_type = "Review_User_Ticket_User"

        """ Affiche le ticket ( sans réponse ) de l'utilisateur connecté """
        if ticket_user.response == '0':
            ticket_user.entry_type = "Ticket_User_Not_Response"

    entries = sorted(chain(tickets_user, tickets_user_follow, reviews_user, reviews_user_follow),
                     key=lambda x: x.date_created, reverse=True)
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


@login_required
def image_question(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)

    return render(request, 'blog/image_question.html', context={'ticket': ticket})


@login_required
def ticket_delete(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    if request.method == 'POST':
        if ticket:
            ticket.delete()
            return redirect('posts')

    context6 = {
        'ticket': ticket,
    }
    return render(request, 'blog/ticket_delete.html', context=context6)


@login_required
def review_delete(request, review_id):
    review = get_object_or_404(models.Review, id=review_id)
    ticket_id = review.ticket_id
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    if request.method == 'POST':
        if review:
            ticket.response = 0
            ticket.save()
            review.delete()
            return redirect('posts')
    context7 = {
        'review': review,
    }
    return render(request, 'blog/review_delete.html', context=context7)


@login_required
def edit_ticket_not_response1(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    photo_form = forms.PhotoForm()
    edit_ticket_form = forms.TicketForm(instance=ticket)
    if request.method == 'POST':
        edit_ticket_form = forms.TicketForm(request.POST, instance=ticket)
        photo_form = forms.PhotoForm(request.POST, request.FILES)
        if edit_ticket_form.is_valid():
            ticket.save()
            return redirect('posts')

    context5 = {
        'edit_ticket_form': edit_ticket_form,
        'ticket': ticket,
        'photo_form': photo_form,
    }
    return render(request, 'blog/edit_ticket_not_response1.html', context=context5)


@login_required
def edit_ticket_not_response(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    photo_form = forms.PhotoForm()
    edit_ticket_form = forms.TicketForm(instance=ticket)
    if request.method == 'POST':
        edit_ticket_form = forms.TicketForm(request.POST, instance=ticket)
        photo_form = forms.PhotoForm(request.POST, request.FILES)
        if edit_ticket_form.is_valid():
            ticket = edit_ticket_form.save(commit=False)
            ticket.user = request.user
            if photo_form:
                photo = photo_form.save(commit=False)
                photo.uploader = request.user
                photo.save()
                ticket.photo = photo
                ticket.save()
                return redirect('posts')

    context5 = {
        'edit_ticket_form': edit_ticket_form,
        'ticket': ticket,
        'photo_form': photo_form,
    }
    return render(request, 'blog/edit_ticket_not_response.html', context=context5)


# blog\views.py
@login_required
def follow_users(request):

    """ Récupère la liste des utilisateurs inscrits"""
    form = forms.FollowUsersForm(instance=request.user)

    """ Récupère la liste de mes abonnements depuis la classe DeleteFollowingForm"""
    del_following = forms.DeleteFollowingForm(user=request.user)

    """ Récupère la liste de mes abonnements"""
    my_following = request.user.following.all()

    """ Récupère la liste des personnes qui me suivent"""
    my_followers = request.user.follower.all()

    """ Fonctionnalité qui permet d'exclure de la liste, l'utilisateur connecté"""
    form.fields['following'].queryset = form.fields['following'].queryset.exclude(
        username=request.user.username)

    """ Fonctionnalité qui permet de ne pas afficher dans la 'Liste des utilisateurs' mes abonnements"""
    form.fields['following'].queryset = form.fields['following'].queryset.exclude(
        id__in=my_following)

    if request.method == 'POST':
        if 'form' in request.POST:
            form = forms.FollowUsersForm(request.POST, instance=request.user)
            if form.is_valid():
                user = form.save(commit=False)
                """ Récupère l'utilisateur qui a été selectionné dans la liste"""
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
