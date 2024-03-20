from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Post(models.Model):
    Heading = models.CharField(max_length=100)
    Author = models.ForeignKey(User,on_delete = models.CASCADE)  # here we have used User as a foriegn key and models.CASCADE as when we delete the user the related posts should also be deleted.
    PostOn = models.DateTimeField(default=timezone.now) # There are many ways to send as parameter to datetime field, but i particularly used this one so that the time and date will be updated each time the data is updated.
    Description = models.TextField()

    # this will return the heading of the post when you print the objects.
    def __str__(self) -> str:
        return self.Heading
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={'pk': self.pk})
        # return reverse('post_home')

    def save(self, *args, **kwargs):
        # Update PostOn only if the post is being edited and not newly created
        if self.pk:
            self.PostOn = timezone.now()
        super().save(*args, **kwargs)


