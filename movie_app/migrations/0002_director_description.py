# Generated by Django 3.2.7 on 2022-07-21 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='director',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]