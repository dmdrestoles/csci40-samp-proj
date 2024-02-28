from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class ArticleCategory(models.Model):

    code_id = models.CharField(max_length=15)
    name = models.CharField(max_length=31)
    descn = models.TextField()

    class Meta:
        ordering = ['name']


class Article(models.Model):

    title = models.CharField(max_length=255)
    namespace = models.CharField(max_length=255)
    author = models.ForeignKey(User, 
                               on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(ArticleCategory, 
                                 on_delete=models.SET_NULL, null=True)
    entry = models.TextField()
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Article, self).save(*args, **kwargs)

    class Meta:
        ordering = ['title']
