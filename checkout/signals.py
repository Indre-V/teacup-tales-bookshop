"""Signals file imports"""
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem

@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create
    """
    # Ensure you are calling the correct method to update the total
    instance.order.get_total()  # Correct method name from the Order model

@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total on lineitem delete
    """
    # Ensure you are calling the correct method to update the total
    instance.order.get_total()  # Correct method name from the Order model

