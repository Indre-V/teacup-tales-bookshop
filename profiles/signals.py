"""Imports for signals file"""
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile


# pylint: disable=locally-disabled, no-member
# pylint: disable=unused-argument

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Signal handler to create a user profile when a new user is created.
    """
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    Signal handler to save a user profile when a new user is created.
    """
    instance.userprofile.save()

models.signals.post_save.connect(create_user_profile, sender=User)
