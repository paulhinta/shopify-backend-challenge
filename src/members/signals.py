from django.db.models.signals import post_save
from django.contrib.auth.models import User #sender
from django.dispath import receiver
from .models import Profile

#creates a profile for each new User
def create_profile(sender, instance, create, **kwargs):
    