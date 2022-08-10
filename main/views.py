from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.db.models import Avg
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.views import View



class home(View):
   def get(self, request):
      query = request.GET.get("title")
      allMovies = None
      if query:
         allMovies = Movie.objects.filter(name__icontains=query)
      else:
         allMovies = Movie.objects.all().order_by("name")

      context = {
         "movies": allMovies,
      }

      return render(request, 'main/index.html', context)


class detail(View):
   def get(self, request, id):
      movie = Movie.objects.get(id=id)
      reviews = Review.objects.filter(movie=id).order_by("-date")
      is_favourite = False

      average = reviews.aggregate(Avg("rating"))["rating__avg"]
      if average == None:
         average = 0

      if movie.favourites.filter(id=request.user.id).exists():
         is_favourite = True

      average = round(average, 1)
      context = {
         "movie": movie,
         "reviews": reviews,
         "average": average,
         "is_favourite": is_favourite,
      }

      return render(request, 'main/details.html', context)


class add_movies(View):
   def get(self, request):
      if request.user.is_authenticated:
         if request.user.is_superuser:
            if request.method == "POST":
               form = MovieForm(request.POST or None)

               if form.is_valid():
                  data = form.save(commit=False)
                  data.save()

                  return redirect("main:home")
            else:
               form = MovieForm()
            return render(request, 'main/addmovies.html', {"form": form, "controller": "Add Movie"})
         # if they are not superuser
         else:
            return redirect("main:home")
         # if they are not login
      else:
         return redirect("accounts:login")

   def post(self, request):
      if request.user.is_authenticated:
         if request.user.is_superuser:
            if request.method == "POST":
               form = MovieForm(request.POST or None)

               if form.is_valid():
                  data = form.save(commit=False)
                  data.save()

                  return redirect("main:home")
            else:
               form = MovieForm()
            return render(request, 'main/addmovies.html', {"form": form, "controller": "Add Movie"})
         # if they are not superuser
         else:
            return redirect("main:home")
         # if they are not login
      else:
         return redirect("accounts:login")


class edit_movies(View):
   def get(self, request, id):
      if request.user.is_authenticated:
         if request.user.is_superuser:
            movie = Movie.objects.get(id=id)


            form = MovieForm(instance=movie)
            return render(request, "main/addmovies.html", {"form": form, "controller": "Edit Movie"})
         # if they are not superuser
         else:
            return redirect("main:home")
         # if they are not login
      else:
         return redirect("accounts:login")

   def post(self, request, id):
      if request.user.is_authenticated:
         if request.user.is_superuser:
            movie = Movie.objects.get(id=id)


            form = MovieForm(request.POST or None, instance=movie)

            if form.is_valid():
               data = form.save(commit=False)
               data.save()
               return redirect("main:detail", id)

            return render(request, "main/addmovies.html", {"form": form, "controller": "Edit Movie"})
         # if they are not superuser
         else:
            return redirect("main:home")
         # if they are not login
      else:
         return redirect("accounts:login")


class delete_movies(View):
   def get(self, request, id):
      if request.user.is_authenticated:
         if request.user.is_superuser:
            movie = Movie.objects.get(id=id)

            movie.delete()
            return redirect("main:home")
         # if they are not superuser
         else:
            return redirect("main:home")
      # if they are not login
      else:
         return redirect("accounts:login")


class add_review(View):
   def get(self, request, id):
      if request.user.is_authenticated:
         movie = Movie.objects.get(id=id)

         return render(request, 'main/details.html', {"form": form})
      else:
         return redirect("accounts:login")

   def post(self, request, id):
      if request.user.is_authenticated:
         movie = Movie.objects.get(id=id)

         form = ReviewForm(request.POST or None)
         if form.is_valid():
            data = form.save(commit=False)
            data.comment = request.POST["comment"]
            data.rating = request.POST["rating"]
            data.user = request.user
            data.movie = movie
            data.save()
            return redirect("main:detail", id)


         return render(request, 'main/details.html', {"form": form})
      else:
         return redirect("accounts:login")


class edit_review(View):
   def get(self, request, movie_id, review_id):
      if request.user.is_authenticated:
         movie = Movie.objects.get(id=movie_id)
         review = Review.objects.get(movie=movie, id=review_id)

         if request.user == review.user:


            return render(request, 'main/editreview.html', {"form": form})
         else:
            return redirect("main:detail", movie_id)
      else:
         return redirect("accounts:login")

   def post(self, request, movie_id, review_id):
      if request.user.is_authenticated:
         movie = Movie.objects.get(id=movie_id)
         review = Review.objects.get(movie=movie, id=review_id)

         if request.user == review.user:

            form = ReviewForm(request.POST, instance=review)
            if form.is_valid():
               data = form.save(commit=False)
               if (data.rating > 10) or (data.rating < 0):
                  error = "Out of range. Please select rating from 0 to 10."
                  return render(request, 'main/editreview.html', {"error": error, "form": form})
               else:
                  data.save()
                  return redirect("main:detail", movie_id)

            return render(request, 'main/editreview.html', {"form": form})
         else:
            return redirect("main:detail", movie_id)
      else:
         return redirect("accounts:login")


class delete_review(View):
   def get(self, request, movie_id, review_id):
         movie = Movie.objects.get(id=movie_id)
         review = Review.objects.get(movie=movie, id=review_id)

         if request.user == review.user:

           review.delete()

         return redirect("main:detail", movie_id)


class favourites_add(View):
   def get(self, request, id):
      movie = get_object_or_404(Movie, id=id)
      if movie.favourites.filter(id=request.user.id).exists():
         movie.favourites.remove(request.user)
      else:
         movie.favourites.add(request.user)

      return HttpResponseRedirect(request.META['HTTP_REFERER'])


class favourites_list(View):
   def get(self, request):
      user = request.user
      favourites_add = user.favourite.all()

      context = {
         'favourites_add': favourites_add,
      }

      return render(request, 'main/favourite_list.html', context)













