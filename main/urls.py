
from django.urls import path
from . import views


app_name = "main"

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('', views.HomeUnView.as_view(), name="home"),
    path('details/<int:id>/', views.DetailView.as_view(), name="detail"),
    path('addmovies/', views.AddMoviesView.as_view(), name="add_movies"),
    path('editmovies/<int:id>/', views.EditMoviesView.as_view(), name="edit_movies"),
    path('deletemovie/<int:id>', views.DeleteMoviesView.as_view(), name="delete_movies"),
    path('addreview/<int:id>/', views.AddReviewView.as_view(), name="add_review"),
    path('editreview/<int:movie_id>/<int:review_id>/', views.EditReviewView.as_view(), name="edit_review"),
    path('deletereview/<int:movie_id>/<int:review_id>/', views.DeleteReviewView.as_view(), name="delete_review"),
    path('<int:id>/favourites_add/$', views.FavouritesAddView.as_view(), name='favourites_add'),
    path('favourites_list/', views.FavouritesListView.as_view(), name="favourite_list"),
    path('my-review/', views.MyReview.as_view(), name='my-review'),
    path("theatres/", views.InTheatres.as_view(), name="theatres"),
    path("detail/<int:movie_id>/", views.TDetailView.as_view(), name="movie_detail"),


]