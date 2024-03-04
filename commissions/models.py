from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class CommissionCategory(models.Model):
    code_id = models.CharField(max_length=15)
    name = models.CharField(max_length=31)
    descn = models.TextField()

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Commission categories"


class Commission(models.Model):
    title = models.CharField(max_length=255)
    namespace = models.CharField(max_length=255)
    category = models.ForeignKey(CommissionCategory,
                              on_delete=models.SET_NULL, null=True)
    manpower_required = models.IntegerField()
    manpower_signed = models.IntegerField()
    descn = models.TextField()
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Commission, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-updated']


class Comment(models.Model):
    commission = models.ForeignKey(Commission, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Comment, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created']
