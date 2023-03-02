from django.shortcuts import render, redirect
from django.utils.text import slugify
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.views import View


class RegisterView(View):
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

                #user = authenticate(username=user.username, password=raw_password)
                #slug = slugify(user.username)
                #new_profile = UserProfile(user= user, slug=slug)
                #new_profile.save()

                login(request, user)

                return redirect("main:home")

            return render(request, "accounts/register.html", {"form": form})


class LoginUserView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("main:home")
        else:

            return render(request, 'accounts/login.html')

    def post(self, request):
        if request.user.is_authenticated:
            return redirect("main:home")
        else:

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


class LogoutUserView(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            print("Logged out succesfully")
            return redirect("accounts:login")
        else:
            return redirect("accounts:login")


class ProfileView(View):
    def get(self, request):
        return render(request, 'accounts/profile.html')

#class ProfileView(View):
#   def get(self, request, slug):
#       user = UserProfile.objects.get(slug=slug)
#       context = {
#           'user': user
#       }
#       return render(request, 'accounts/profile.html', context)


class EditProfileView(View):
    def get(self, request):
        profile = UserProfile.objects.get_or_create(user=request.user)
        form = EditProfileForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.userprofile)
        args = {}
        args['form'] = form
        args['profile_form'] = profile_form
        return render(request, 'accounts/edit_profile.html', args)

    def post(self, request):
        profile = UserProfile.objects.get_or_create(user=request.user)
        form = EditProfileForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.userprofile)

        if form.is_valid() and profile_form.is_valid():
            user_form = form.save()
            custom_form = profile_form.save(False)
            custom_form.user = user_form
            custom_form.save()
            return redirect('accounts:profile')
