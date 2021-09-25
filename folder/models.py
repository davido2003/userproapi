from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=100)
    images = models.ImageField('images/')
    date = models.DateField()
    description = models.TextField(max_length=10000)


    def __str__(self):
        return self.title

