from django.db import models
#
# # Create your models here.
#
class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    duration = models.CharField(max_length=100)
    director = models.ForeignKey(Director, on_delete=models.CASCADE,
                                related_name='movies'
                                 )




    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.TextField(blank=True)
    movie = models.ForeignKey(Movie,
                              on_delete=models.CASCADE,
                                related_name='reviews')
    stars = models.IntegerField(default=1)

    def __str__(self):
        return self.text










# Movie
# title
# description
# duration
# director(ForeignKey)
