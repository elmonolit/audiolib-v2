from django.urls import path
from . import views

urlpatterns = [
    path('',views.MainView.as_view(), name='main'),
    path('artists/<slug:slug>/',views.ArtistDetailView.as_view(), name='artist_detail'),
    path('bands/<slug:slug>/',views.BandDetailView.as_view(), name='band_detail'),
    path('genre/<slug:slug>/', views.GenreDetailView.as_view(), name='genre_detail'),
    path('reg/', views.registration, name = 'registration'),
    path('artist_create', views.ArtistCreate.as_view(), name='artist_create'),
    path('band_create', views.BandCreate.as_view(), name='band_create'),
    path('genre_create', views.GenreCreate.as_view(), name='genre_create'),
    path('search/', views.search, name='search'),

]