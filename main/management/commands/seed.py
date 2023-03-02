import requests
from django.core.management.base import BaseCommand
from ...models import Movie



def get_movie(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=2a5466b9dc7b1cc2e8ec0de89645fc1e&language=en-US'
    m = requests.get(url, headers={'Content-Type': 'application/json'})
    movie = m.json()
    print(movie)
    return movie

def seed_movie():
    for num in range(1, 790000):
        try:
            movie = get_movie(num)
            Movie.objects.create(
                name=movie["title"],
                original=movie["original_title"],
                status=movie["status"],
                description=movie["overview"],
                release_date=movie["release_date"],
                averageRating=movie["vote_average"],
                image=movie["poster_path"],
                category=movie["genres"],
                language=movie["spoken_languages"],
                tagline=movie["tagline"],
                time=movie["runtime"]
            )
        except KeyError:
            continue



def clear_data():
  Movie.objects.all().delete()


class Command(BaseCommand):
     def handle(self, *args, **options):
        seed_movie()
        #clear_data()
        print("completed")