from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# Most importantly this signals.py file is created to create a profile for a user
# soon when the user is register. So when the user is saved the receiver will get the signal
# which will be activated on user saves and then profile of user created. and same with saveprofile.

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()