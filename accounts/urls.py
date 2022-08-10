from django.urls import path
from . import views


app_name = "accounts"

urlpatterns = [
    path("register/", views.register.as_view(), name="register"),
    path("login/", views.login_user.as_view(), name="login"),
    path("logout/", views.logout_user.as_view(), name="logout"),
    path('profile/', views.profile.as_view(), name='profile'),

]