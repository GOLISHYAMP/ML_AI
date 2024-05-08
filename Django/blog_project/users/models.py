from typing import Iterable, Optional
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    def __str__(self):
        return f"{self.user.username} profile"
    
    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)

        pic = Image.open(self.profile_pic.path)
        if self.profile_pic.height > 300 and self.profile_pic.width > 300:
            output_size = (300, 300)
            pic.thumbnail(output_size)
            pic.save(self.profile_pic.path)