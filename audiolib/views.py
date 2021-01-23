from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import Artist, Genre, Band
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from .forms import UserForm, ArtistForm, BandForm, GenreForm
from django.contrib.auth import authenticate, login
from django.urls import reverse


class MainView(ListView):
    model = Artist
    template_name = 'audiolib/main.html'

    def get_context_data(self, **kwargs):
        kwargs = super(MainView, self).get_context_data()
        kwargs.update(
            {
                'genre_list': Genre.objects.all(),
                'band_list' : Band.objects.all(),

            }
        )
        return kwargs

class ArtistDetailView(DetailView):
    model = Artist
    slug_field = 'slug'

class BandDetailView(DetailView):
    model = Band
    slug_field = 'slug'
class GenreDetailView(DetailView):
    model = Genre
    slug_field = 'slug'

def registration(request):
    registrated = False
    if request.method == 'POST':
        user_form = UserForm(data = request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request, 'audiolib/reg.html',{
        'user_form': user_form,
        'registrated': registrated
    })
class ArtistCreate(View):
    def post(self,request):
        form = ArtistForm(request.POST, request.FILES)
        # form.photo = request.FILES['photo']
        if form.is_valid():
            artist = form.save()
            return HttpResponseRedirect(reverse('artist_detail', args=[artist.slug]))
        else:
            print(form.errors)
            return HttpResponse(form.errors)
    def get(self,request):
        form = ArtistForm()
        return render(request,'audiolib/artist_create.html',{'form':form})

class BandCreate(View):
    def get(self,request):
        form = BandForm()
        return render(request,'audiolib/band_create.html',{'form':form})
    def post(self,request):
        form = BandForm(request.POST, request.FILES)
        if form.is_valid():
            band = form.save()
            return HttpResponseRedirect(reverse('band_detail', args=[band.slug]))
        else:
            print(form.errors)
            return HttpResponse(form.errors)

class GenreCreate(View):
    def get(self,request):
        form = GenreForm()
        return render(request, 'audiolib/genre_create.html')
    def post(self,request):
        form = GenreForm(request.POST)
        if form.is_valid():
            genre = form.save()
            return HttpResponseRedirect(reverse('genre_detail', args=[genre.slug]))

def get_list(max_res, starts_with=''):
    band_list = []
    if starts_with:
        band_list = Band.objects.filter(name__istartswith=starts_with)

    if max_res > 0:
        if len(band_list) > max_res:
            band_list = band_list[:max_res]
    return band_list


def search(request):
    band_list = []
    if 'search' in request.GET:
        starts_with = request.GET['search']
        band_list = get_list(8, starts_with)
    return render(request,'audiolib/e.html',{'band_list': band_list})




