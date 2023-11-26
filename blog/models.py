from django.db import models
from django.utils.timezone import now



class BlogInfo(models.Model):
    blog_id = models.AutoField(primary_key=True)
    blog_name = models.CharField(max_length=50)
    blog_likes = models.IntegerField(default=0)
    blog_hates = models.IntegerField(default=0)
    blog_reads = models.IntegerField(default=0)
    blog_date = models.DateField(default=now)
    blog_category = models.CharField(max_length=50)
    blog_description = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.blog_name} (ID: {self.blog_id})"