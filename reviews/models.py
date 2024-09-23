"""Review models imports"""
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from products.models import Product

# pylint: disable=locally-disabled, no-member

RATING = (
    (1,  "★☆☆☆☆"),
    (2,  "★★☆☆☆"),
    (3,  "★★★☆☆"),
    (4,  "★★★★☆"),
    (5,  "★★★★★"),
)

class Review(models.Model):
    """
    Model representing product reviews by users
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    content = models.TextField(max_length=300, blank=True)
    rating = models.IntegerField(choices=RATING, default=None)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        super().clean()
        if self.rating is not None:
            validators = [
                MinValueValidator(1, message="Rating must be at least 1."),
                MaxValueValidator(5, message="Rating must be at most 5."),
            ]
            for validator in validators:
                validator(self.rating)

    class Meta:
        """
        Sets the order of comments by date ascending
        """

        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.content} by {self.user.username}"
