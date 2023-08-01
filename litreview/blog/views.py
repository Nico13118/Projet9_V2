from django.shortcuts import render, redirect
from . import forms, models
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request, 'blog/home.html')


@login_required
def flow(request):
    photos = models.Photo.objects.all()
    blogs = models.Blog.objects.all()
    return render(request, 'blog/flow.html', context={'photos': photos, 'blogs': blogs})

@login_required
def request_review(request):
    blog_form = forms.BlogForm()
    photo_form = forms.PhotoForm()
    if request.method == 'POST':
        blog_form = forms.BlogForm(request.POST)
        photo_form = forms.PhotoForm(request.POST, request.FILES)
        if all([blog_form.is_valid(), photo_form.is_valid()]):
            photo = photo_form.save(commit=False)
            photo.uploader = request.user
            photo.save()
            blog = blog_form.save(commit=False)
            blog.author = request.user
            blog.photo = photo
            blog.save()
            return redirect('flow')
    context = {
        'blog_form': blog_form,
        'photo_form': photo_form,
    }
    return render(request, 'blog/request_review.html', context=context)


@login_required
def create_ticket(request):
    return render(request, 'blog/create_ticket.html')
