from django.db import models

class Post(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField()
    published_date = models.DateTimeField()
    image = models.ImageField(upload_to='blog_image/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        return self.title



