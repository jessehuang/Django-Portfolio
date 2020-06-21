from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Notebook(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    starter = models.ForeignKey(User, related_name='notebook',on_delete=models.PROTECT, null=True)


class Page(models.Model):
    message = models.TextField(max_length=4095)
    notebook = models.ForeignKey(Notebook, related_name='page',on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='page',on_delete=models.PROTECT)