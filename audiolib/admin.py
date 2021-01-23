from django.contrib import admin
from .models import Artist, Band, Genre, UserProfile

class ArtistAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Artist)
admin.site.register(Band)
admin.site.register(Genre)
admin.site.register(UserProfile)


# Register your models here.
