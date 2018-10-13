from django.db import models

# Create your models here.
class Article(models.Model):
    id = models.IntegerField(primary_key=True,auto_created=True)
    title = models.CharField(max_length=40)
    type = models.CharField(max_length=20)
    content = models.TextField()
    post_time = models.DateTimeField(auto_now=True)
    see_count = models.IntegerField(default=0)
    like = models.IntegerField(default=0)


    def __str__(self):
        return self.title