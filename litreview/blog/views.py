from django.shortcuts import render, redirect
from . import forms, models
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request, 'blog/home.html')


@login_required
def flow(request):
    photos = models.Photo.objects.all()
    tickets = models.Ticket.objects.all()
    reviews = models.Review.objects.all()

    tickets_photos = zip(tickets, photos)
    return render(request, 'blog/flow.html', context={'tickets_photos': tickets_photos, 'reviews': reviews})


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
def create_review_not_in_response(request):
    review_form = forms.ReviewForm()
    photo_form = forms.PhotoForm()
    if request.method == 'POST':
        review_form = forms.ReviewForm(request.POST)
        photo_form = forms.PhotoForm(request.POST, request.FILES)
        if all([review_form.is_valid(), photo_form.is_valid()]):
            photo = photo_form.save(commit=False)
            photo.uploader = request.user
            photo.save()
            review = review_form.save(commit=False)
            review.user = request.user
            review.photo = photo
            review.save()
            return redirect('flow')
    context2 = {
        'review_form': review_form,
        'photo_form': photo_form,
    }
    return render(request, 'blog/create_review_not_in_response.html', context=context2)
