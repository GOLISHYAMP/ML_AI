from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    # if the user do not enter any image then this default.jpg in the media folder will be show 
    # if the user give the pic then it will be stored in the profile_pic folder inside media folder
    image = models.ImageField(default='default.jpg', upload_to = 'profile_pic' )

    def __str__(self):
        return f'{self.user.username} profile'
    
    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if self.image.height > 300 and self.image.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)