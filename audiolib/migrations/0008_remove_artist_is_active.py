# Generated by Django 3.1.1 on 2021-01-22 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('audiolib', '0007_artist_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='is_active',
        ),
    ]
