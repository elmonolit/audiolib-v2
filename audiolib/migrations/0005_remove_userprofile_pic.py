# Generated by Django 3.1.1 on 2020-09-09 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('audiolib', '0004_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='pic',
        ),
    ]
