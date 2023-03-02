from django import forms
from .models import *


class MovieForm(forms.ModelForm):
    director = forms.CharField(required=False)
    cast = forms.CharField(required=False)
    class Meta:
        model = Movie
        fields = (
            'name', 'original', 'time', 'status', 'category', 'language', 'tagline', 'description',
            'release_date', 'image', 'director', 'cast'
        )

        # choices = Category.objects.all().values_list('name', 'name').order_by("name")
        # choice_list = []
        # for item in choices:
        #   choice_list.append(item)

        widgets = {
            # 'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
        }



class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('comment', 'rating')
