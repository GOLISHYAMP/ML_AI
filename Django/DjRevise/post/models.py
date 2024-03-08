from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Post(models.Model):
    Heading = models.CharField(max_length=100)
    Author = models.ForeignKey(User,on_delete = models.CASCADE)
    PostOn = models.DateTimeField(default=timezone.now)
    Description = models.TextField()

    def __str__(self) -> str:
        return self.Heading
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={'pk': self.pk})
        # return reverse('post_home')


