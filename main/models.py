from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


class Movie(models.Model):
    name = models.CharField(max_length=300)
    director = models.CharField(max_length=300)
    cast = models.CharField(max_length=800)
    description = models.TextField(max_length=5000)
    release_date = models.DateField()
    averageRating = models.FloatField(default=0)
    image = models.URLField(default=None, null=True)
    category = models.CharField(max_length=300, default='Uncategorized')
    favourites = models.ManyToManyField(User, related_name='favourite', default=None, blank=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main:detail', args=[self.id])


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000)
    rating = models.FloatField(default=0)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('index')

