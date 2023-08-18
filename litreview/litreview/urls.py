"""
URL configuration for litreview project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import authentication.views
import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("login/", authentication.views.LoginPageView.as_view(), name='login'),
    path('logout/', authentication.views.logout_user, name='logout'),
    path('home/', blog.views.home, name='home'),
    path('flow/', blog.views.flow, name='flow'),
    path('review_in_response/<int:ticket_id>', blog.views.review_in_response, name='review_in_response'),
    path('review_not_in_response/', blog.views.review_not_in_response,
         name='review_not_in_response'),
    path('posts/', blog.views.posts, name='posts'),
    path('subscriptions/', blog.views.follow_users, name='subscriptions'),

    path('create_ticket/', blog.views.create_ticket, name='create_ticket'),
    path('signup/', authentication.views.signup_page, name='signup'),
    path('success/', authentication.views.registration_success, name='success'),
    path('password_reset_form/', authentication.views.CustomPasswordResetView.as_view(), name='password_reset_form'),
    path('password_reset_email/', authentication.views.CustomPasswordResetView.as_view(), name='password_reset_email'),
    path('password_reset_confirm/<uidb64>/<token>/',
         authentication.views.CustomPasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('password_reset_complete/', authentication.views.password_reset_complete, name='password_reset_complete'),
    path('password_reset_done/', authentication.views.password_reset_done, name='password_reset_done'),

]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
