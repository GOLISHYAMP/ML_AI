from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    Heading = models.TextField()
    Author = models.ForeignKey(User,on_delete = models.CASCADE)
    PostOn = models.DateTimeField(default=timezone.now)
    Description = models.TextField()

    def __str__(self) -> str:
        return self.Heading


