
from django.urls import path
from . import views


app_name = "main"

urlpatterns = [
    path('', views.home.as_view(), name="home"),
    path('details/<int:id>/', views.detail.as_view(), name="detail"),
    path('addmovies/', views.add_movies.as_view(), name="add_movies"),
    path('editmovies/<int:id>/', views.edit_movies.as_view(), name="edit_movies"),
    path('deletemovie/<int:id>', views.delete_movies.as_view(), name="delete_movies"),
    path('addreview/<int:id>/', views.add_review.as_view(), name="add_review"),
    path('editreview/<int:movie_id>/<int:review_id>/', views.edit_review.as_view(), name="edit_review"),
    path('deletereview/<int:movie_id>/<int:review_id>/', views.delete_review.as_view(), name="delete_review"),
    path('<int:id>/favourites_add/$', views.favourites_add.as_view(), name='favourites_add'),
    path('favourites_list/', views.favourites_list.as_view(), name="favourite_list"),


]