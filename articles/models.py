from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255)
    content_snippet = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
