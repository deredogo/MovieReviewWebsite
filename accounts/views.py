from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from main.models import *
from django.views import View



class register(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("main:home")
            # if they are not logged in
        else:

            form = RegistrationForm()
        return render(request, "accounts/register.html", {"form": form})

    def post(self, request):
        if request.user.is_authenticated:
            return redirect("main:home")
            # if they are not logged in
        else:

            form = RegistrationForm(request.POST or None)

            if form.is_valid():
                user = form.save()

                raw_password = form.cleaned_data.get('password1')

                user = authenticate(username=user.username, password=raw_password)

                login(request, user)

                return redirect("main:home")


            return render(request, "accounts/register.html", {"form": form})


class login_user(View):
    def get (self, request):
        if request.user.is_authenticated:
            return redirect("main:home")
        else:
            if request.method == "POST":
                username = request.POST["username"]
                password = request.POST["password"]

                print(username, password)
                user = authenticate(username=username, password=password)

                if user is not None:
                    print("password")
                    if user.is_active:
                        login(request, user)
                        return redirect("main:home")
                    else:
                        return render(request, 'accounts/login.html', {"error": "Your account has been disabled."})
                else:
                    return render(request, 'accounts/login.html', {"error": "Invalid Username or Password. Try Again."})

            return render(request, 'accounts/login.html')

    def post(self, request):
        if request.user.is_authenticated:
            return redirect("main:home")
        else:
            if request.method == "POST":
                username = request.POST["username"]
                password = request.POST["password"]

                print(username, password)
                user = authenticate(username=username, password=password)

                if user is not None:
                    print("password")
                    if user.is_active:
                        login(request, user)
                        return redirect("main:home")
                    else:
                        return render(request, 'accounts/login.html', {"error": "Your account has been disabled."})
                else:
                    return render(request, 'accounts/login.html', {"error": "Invalid Username or Password. Try Again."})

            return render(request, 'accounts/login.html')


class logout_user(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            print("Logged out succesfully")
            return redirect("accounts:login")
        else:
            return redirect("accounts:login")


class profile(View):
     def get(self, request):
        return render(request, 'accounts/profile.html')



