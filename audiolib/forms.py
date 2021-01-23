from django import forms
# from .models import UserProfile
from django.contrib.auth.models import User
from .models import Artist, Band, Genre

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        exclude = ('slug',)

class BandForm(forms.ModelForm):
    # slug = forms.CharField(widget=forms.HiddenInput,required=False)
    class Meta:
        model = Band
        exclude = ( 'artist', 'slug')

class GenreForm(forms.ModelForm):

    class Meta:
        model = Genre
        exclude = ('slug',)

