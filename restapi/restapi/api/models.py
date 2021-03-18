from django.db import models

# Create your models here.
class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=20)
    weekend = models.CharField(max_length=20)
    gross = models.CharField(max_length=20)
    weeks = models.CharField(max_length=20)
    genre = models.CharField(max_length=100)
    rating = models.CharField(max_length=10)
    movie_release = models.CharField(max_length=20)
    people = models.CharField(max_length=20)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movie'


class MyTopicMovie(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.TextField()
    weekend = models.TextField()
    gross = models.TextField()
    weeks = models.TextField()
    genre = models.TextField()
    rating = models.TextField()
    movie_release = models.TextField()
    people = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'my_topic_movie'


class MyTopicUsers(models.Model):
    title = models.TextField()
    weekend = models.TextField()
    gross = models.TextField()
    weeks = models.TextField()
    genre = models.TextField()
    rating = models.TextField()
    movie_release = models.TextField()
    people = models.TextField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'my_topic_users'


class Stock(models.Model):
    stock_rank = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    price = models.CharField(max_length=20)
    ratio_updown = models.CharField(max_length=5)
    ratio = models.CharField(max_length=10)
    low = models.CharField(max_length=10)
    volume = models.CharField(max_length=10)
    payment = models.CharField(max_length=20)
    buy = models.CharField(max_length=20)
    sell = models.CharField(max_length=20)
    capitalization = models.CharField(max_length=20)
    per = models.CharField(max_length=20)
    roe = models.CharField(max_length=20)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock'


class TopicStock(models.Model):
    id = models.IntegerField(primary_key=True)
    stock_rank = models.TextField()
    title = models.TextField()
    price = models.TextField()
    low = models.TextField()
    volume = models.TextField()
    payment = models.TextField()
    buy = models.TextField()
    sell = models.TextField()
    capitalization = models.TextField()
    per = models.TextField()
    roe = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'topic_stock'


class Users(models.Model):
    title = models.CharField(max_length=20)
    weekend = models.CharField(max_length=20)
    gross = models.CharField(max_length=20)
    weeks = models.CharField(max_length=20)
    genre = models.CharField(max_length=100)
    movie_release = models.CharField(max_length=20)
    rating = models.CharField(max_length=10)
    people = models.CharField(max_length=20)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'