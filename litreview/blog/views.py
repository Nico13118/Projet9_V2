from django.shortcuts import render, redirect, get_object_or_404
from . import forms, models
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    reviews = models.Review.objects.all()
    tickets_reviews = models.Review.objects.all()

    return render(request, 'blog/flow.html', context={'tickets_reviews': tickets_reviews})


@login_required
def flow(request):
    photos = models.Photo.objects.all()
    tickets = models.Ticket.objects.all()
    reviews = models.Review.objects.all()

    tickets_photos = zip(tickets, photos)
    tickets_reviews = zip(tickets, reviews)
    return render(request, 'blog/flow.html', context={'tickets_photos': tickets_photos,
                                                      'tickets_reviews': tickets_reviews})


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
            ticket.save()
            review = review_form.save(commit=False)
            review.user = request.user
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
    edit_form = forms.TicketForm(instance=ticket)
    review_form = forms.ReviewResponseForm()
    if request.method == 'POST':
        if 'review_in_response' in request.POST:
            edit_form = forms.TicketForm(request.POST, instance=ticket)
            review_form = forms.ReviewResponseForm(request.POST)
            if all([edit_form.is_valid(), review_form.is_valid()]):
                ticket = edit_form.save(commit=False)
                ticket.save()
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
        'edit_form': edit_form,
        'ticket': ticket,
    }
    return render(request, 'blog/review_in_response.html', context=context3)

