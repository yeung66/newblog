from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=40)
    type = models.CharField(max_length=20)
    content = models.TextField()

    def __str__(self):
        return self.title