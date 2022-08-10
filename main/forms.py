from django import forms
from .models import *

choices = Category.objects.all().values_list('name','name').order_by("name")

choice_list = []

for item in choices:
    choice_list.append(item)

#add movie form
class MovieForm (forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('name', 'director', 'cast', 'category', 'description', 'release_date', 'image')


        widgets = {
            'category': forms.Select(choices=choice_list,attrs={'class': 'form-control'}),
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('comment', 'rating')


