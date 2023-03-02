import json

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
import jsonfield


class Movie(models.Model):
    name = models.CharField(max_length=300)
    original = models.CharField(max_length=300, default='')
    status = models.CharField(max_length=100, default='')
    time = models.IntegerField(default=1, blank=True, null=True)
    director = models.CharField(max_length=300)
    cast = models.CharField(max_length=800, blank=True)
    description = models.TextField(max_length=5000)
    tagline = models.TextField(max_length=1000, default='')
    release_date = models.DateField()
    averageRating = models.FloatField(default=0)
    image = models.ImageField(default=None, null=True)
    category = jsonfield.JSONField(default=dict)
    language = jsonfield.JSONField()
    favourites = models.ManyToManyField(User, related_name='favourite', default=None, blank=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main:detail', args=[self.id])

    def get_category(self):
        print(self.category, type(self.category))
        return ', '.join([category['name'] for category in json.loads(str(self.category))])

    def get_language(self):
        print(self.language, type(self.language))
        return ', '.join([language['english_name'] for language in json.loads(str(self.language))])


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000)
    rating = models.FloatField(default=0)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.user.username

# class Category(models.Model):
#    name = models.CharField(max_length=300)
#   def __str__(self):
#      return self.name

#   def get_absolute_url(self):
#      return reverse('index')
