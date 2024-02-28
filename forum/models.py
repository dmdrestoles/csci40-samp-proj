from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class ThreadCategory(models.Model):
    code_id = models.CharField(max_length=15)
    name = models.CharField(max_length=31)
    descn = models.TextField()

    class Meta:
        ordering = ['name']


class Thread(models.Model):
    title = models.CharField(max_length=255)
    namespace = models.CharField(max_length=255)
    category = ThreadCategory(ThreadCategory,
                              on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Thread, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-updated']


class Post(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['created']
