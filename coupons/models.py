"""Coupons model import"""
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

class Coupon(models.Model):
    """
    Model representing a discount coupon.
    """
    DISCOUNT_TYPE_CHOICES = (
        ('percentage', 'Percentage'),
        ('amount', 'Amount'),
    )

    code = models.CharField(max_length=50, unique=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount_type = models.CharField(max_length=10, choices=DISCOUNT_TYPE_CHOICES)
    discount_value = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text='Percentage value (0 to 100) or fixed amount'
    )
    active = models.BooleanField(default=True)
    is_used = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.code}"

    def is_valid(self):
        """
        Check if the coupon is valid based on its active status, validity period, and usage.

        Returns:
            bool: True if the coupon is valid, otherwise False.
        """
        now = timezone.now()
        return self.active and not self.is_used and self.valid_from <= now <= self.valid_to
