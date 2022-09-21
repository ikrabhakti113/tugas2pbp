from django.db import models

# Create your modefrom django.db import models

class mywatchlistitem(models.Model):
    watched_movie = models.TextField()
    movie_title = models.TextField()
    movie_rate = models.IntegerField()
    release_date = models.DateField()
    movie_review = models.TextField()