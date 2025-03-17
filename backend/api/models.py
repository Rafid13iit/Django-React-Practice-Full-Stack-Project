from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")



    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True)


class Publisher(models.Model):
    name = models.CharField(max_length=300)


class Book(models.Model):
    name = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    pubdate = models.DateField()


class Store(models.Model):
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(Book)


# from datetime import date

# from django.db import models


# class Blog(models.Model):
#     name = models.CharField(max_length=100)
#     tagline = models.TextField()

#     def __str__(self):
#         return self.name


# class Author(models.Model):
#     name = models.CharField(max_length=200)
#     email = models.EmailField(max_length=255)

#     def __str__(self):
#         return self.name


# class Entry(models.Model):
#     blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
#     headline = models.CharField(max_length=255)
#     body_text = models.TextField()
#     pub_date = models.DateField()
#     mod_date = models.DateField(default=date.today)
#     authors = models.ManyToManyField(Author)
#     number_of_comments = models.IntegerField(default=0)
#     number_of_pingbacks = models.IntegerField(default=0)
#     rating = models.IntegerField(default=5)

#     def __str__(self):
#         return self.headline
    
