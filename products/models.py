"""Imports for Models page"""
import uuid
from decimal import Decimal
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
    author = models.ManyToManyField(Author, related_name='books')
    title = models.CharField(max_length=255)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    isbn = models.CharField(max_length=13, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.FileField(blank=True)
    pages = models.IntegerField(null=True, blank=True)
    publisher = models.CharField(max_length=200)
    type = models.CharField(
        max_length=20, choices=TYPE_CHOICES, default="Hardback")
    date_published = models.DateField()
    stock_amount = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount = models.IntegerField(blank=True, null=True)
    sale_price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    added = models.DateTimeField(auto_now_add=True)

    @property
    def out_of_stock(self):
        """
        Calculate stock flag
        """
        return self.stock_amount <= 0

    def get_final_price(self):
        """
        Returns the price of item based on sale price
        """
        return self.sale_price if self.sale_price else self.price

    def get_discount_amount(self):
        """
        Returns savings
        """
        if self.discount and self.price:
            return self.price * Decimal(self.discount) / Decimal('100')
        return Decimal('0.00')

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
