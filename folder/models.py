from django.db import models

# Create your models here.
class Profile(models.Model):
    title = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()

    def __str__(self):
        return self.title

