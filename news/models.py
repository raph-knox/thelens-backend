from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    body = models.TextField()
    image = models.ImageField(upload_to='article_images/', blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    featured = models.BooleanField(default=False)
    date_published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
