from django.db import models

# Create your models here.
class User(models.Model):
    user = models.CharField(max_length=264)
    email = models.EmailField(unique=True)
    vertify_email = models.EmailField(unique=True)
    def __str__(self):
        return self.user