from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_on = models.DateTimeField(default= timezone.now)

    def __str__(self) -> str:
        return self.title
    
    def  get_absolute_url(self):
        return reverse('detail_blog', kwargs={'pk': self.pk})

