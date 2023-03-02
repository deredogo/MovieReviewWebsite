from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)


app_name = "accounts"

urlpatterns = [
    path("register/", views.RegisterView.as_view(), name="register"),
    path("login/", views.LoginUserView.as_view(), name="login"),
    path("logout/", views.LogoutUserView.as_view(), name="logout"),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    #path('profile/<slug:slug>', views.ProfileView.as_view(), name='profile'),
    path('passreset/', PasswordResetView.as_view(
        template_name='accounts/password_reset.html',
        email_template_name='accounts/password_reset_email.html',
        subject_template_name='accounts/password_reset_subject.txt',
        success_url='/accounts/password_reset/done/'),
         name='password_reset'
         ),
    path('password_reset/done/', PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_done.html'),
         name='password_reset_done'
         ),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='accounts/password_reset_confirm.html',
        success_url='/accounts/reset/done/'),
         name='password_reset_confirm'
         ),
    path('reset/done/', PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html'),
         name='password_reset_complete'
         ),
    path('view_profile/edit_profile/', views.EditProfileView.as_view(), name="edit_profile")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)