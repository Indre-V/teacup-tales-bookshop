"""Imports for Models page"""
import uuid
from django.db import models


# pylint: disable=locally-disabled, no-member

TYPE_CHOICES = [("1", "Hardback"), ("2", "Paperback")]


class Category(models.Model):
    """
    A model to allocate Categories to the books
    """
    name = models.CharField(max_length=200)

    class Meta:
        """
        Options for Category model
        """
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f"{self.name}"


class Author(models.Model):
    """
    Model for authors
    """
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=200)
    bio = models.TextField()

    def __str__(self):
        return f"{self.name}"


class Genre(models.Model):
    """
    A model to define book genre 
    """
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    friendly_name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.name}" or f"{self.friendly_name}"


class Product(models.Model):
    """
    Model for books
    """
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, null=True, blank=True)
    description = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.FileField(blank=True)
    author = models.ManyToManyField(Author, related_name='books')
    publisher = models.CharField(max_length=200)
    type = models.CharField(
        max_length=20, choices=TYPE_CHOICES, default="Hardback")
    date_published = models.DateField()
    pages = models.IntegerField(null=True, blank=True)
    stock_amount = models.IntegerField(default=1)
    out_of_stock = models.BooleanField(default=False)
    on_sale = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount = models.IntegerField(blank=True, null=True)
    sale_price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    added = models.DateTimeField(auto_now_add=True)

    def calc_average_rating(self):
        """
        Calculates average rating for reviews
        """
        reviews = self.review_set.all()
        if reviews:
            return sum(review.rating for review in reviews) / len(reviews)
        return 0

    def __str__(self):
        return f"{self.title}"

