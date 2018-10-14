from django.db import models

# Create your models here.
class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=40,verbose_name='文章标题')
    type = models.CharField(max_length=20,verbose_name='文章分类')
    content = models.TextField(verbose_name='正文内容')
    post_time = models.DateField(auto_now_add=True)
    see_count = models.IntegerField(default=0,verbose_name='阅读人数')
    like = models.IntegerField(default=0,verbose_name='点赞数')


    def __str__(self):
        return self.title