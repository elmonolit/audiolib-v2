from django.db import models
from transliterate import translit
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.contrib.auth.models import User

# class ArtistQuerySet(models.QuerySet):
#     def find_by_nick(self,nick):
#         return self.filter(nickname__icontains=nick)
#
# class ArtistManager(models.Manager):
#
#     def get_queryset(self):
#         return ArtistQuerySet(self.model, using=self._db)
#
#     # def all(self):
#     #     return self.get_queryset().filter(is_active=True)
#
#     def find_by_nick(self,nick):
#         return self.get_queryset().find_by_nick(nick)

class ArtistQuerySet(models.QuerySet):
    def find_nick(self,nick):
        return self.filter(nickname__icontains=nick)

class ArtistManager(models.Manager):

    def get_queryset(self):
        return ArtistQuerySet(self.model,using=self._db)
    #
    # def find_nick(self,nick):
    #     return self.get_queryset().filter(nickname__icontains=nick)
                                                # Artist.objects.get_queryset().find_nick('dio')


class Artist(models.Model):
    nickname = models.CharField('Псевдоним', max_length=100, blank=True)
    first_name = models.CharField('Имя артиста', max_length=100, blank=True)
    second_name = models.CharField('Отчество\Второе имя', max_length=100, blank=True)
    surname = models.CharField('Фамилия артиста', max_length=100, blank=True)
    band = models.ManyToManyField('Band', verbose_name='Группа', related_name='Band', blank=True)
    bio = models.TextField('Биография')
    dob = models.PositiveIntegerField('Дата рождения', default=2020)
    photo = models.ImageField('Фото', upload_to='artists/')
    slug = models.SlugField(max_length=201, unique=True, blank=True)
    objects = ArtistManager()


    def __str__(self):
        if self.nickname == '':
            return f'{self.first_name} {self.surname}'
        else:
            return self.nickname

    def save(self, *args, **kwargs):
        self.slug = slugify(translit(str(self), 'ru', reversed=True))
        super(Artist, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Артист'
        verbose_name_plural = "Артисты"

    def get_absolute_url(self):
        return reverse('artist_detail', kwargs={'slug': self.slug})


class Genre(models.Model):
    name = models.CharField('Название жанра', max_length=100)
    description = models.TextField('Описание')
    artists = models.ManyToManyField(Artist, verbose_name="Артисты", blank=True, related_name='Artists')
    bands = models.ManyToManyField('Band', blank=True, verbose_name='Группы')
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(translit(self.name, 'ru', reversed=True))
        super(Genre, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('genre_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Band(models.Model):
    name = models.CharField('Название группы', max_length=150)
    artist = models.ManyToManyField(Artist, verbose_name='Артисты', blank=True, related_name='band_artists')
    description = models.TextField('Описание')
    logo = models.ImageField('Логотип группы', upload_to='band/')
    slug = models.SlugField(max_length=150, unique=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(translit(self.name, 'ru', reversed=True))
        super(Band, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def get_absolute_url(self):
        return reverse('band_detail', kwargs={'slug': self.slug})


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
