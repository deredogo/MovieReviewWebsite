from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class SexOptions(models.TextChoices):
    FEMALE = 'Female'
    MALE = 'Male'
    OTHERS = 'Others'


class UserProfile(models.Model):
    CHOICES = [('Male', 'Male'),
               ('Female', 'Female')]

    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    bio = models.CharField(max_length=1000, default='')
    image = models.ImageField(upload_to='profile_image', default='profile_pics/default.jpg', blank=True)
    background_Image = models.ImageField(upload_to='background_image', default='profile_pics/default.jpg', blank=True)
    gender = models.CharField(max_length=6, null=True, choices=SexOptions.choices)

    def __str__(self):
        return self.user.username


def createProfile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.created(user=kwargs['instance'])
        post_save.connect(createProfile, sender=User)
