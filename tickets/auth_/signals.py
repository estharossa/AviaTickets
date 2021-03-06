from .models import Profile, MainUser
from django.dispatch import receiver
from django.db.models.signals import post_save


@receiver(post_save, sender=MainUser)
def user_created(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
