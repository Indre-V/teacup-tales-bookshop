"""Profiles app imports"""
from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField

# pylint: disable=locally-disabled, no-member


class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = PhoneNumberField(null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(blank_label='Country', null=True, blank=True)

    def __str__(self):
        return f"{self.user.get_full_name()}" or f"{self.user.email}"


class Wishlist(models.Model):
    """
    Represents a user's wishlist for products.
    """

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="wishlists",
        blank=False,
        null=False,
    )
    product = models.ForeignKey(
        "products.Product",
        on_delete=models.CASCADE,
        related_name="wishlisted_by",
        blank=False,
        null=False,
    )

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"
