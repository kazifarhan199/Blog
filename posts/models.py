from django.db import models



class Post(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    body = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Image(models.Model):
    image = models.ImageField()

    def __str__(self):
        return self.image.url