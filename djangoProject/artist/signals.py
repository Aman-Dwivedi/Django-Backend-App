from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Artist


@receiver(post_save, sender=User)
def create_artist(sender, instance, created, **kwargs):
    if created:
        Artist.objects.create(user=instance, name=instance.username)

