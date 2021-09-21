from django.db import models

# Create your models here.


class Example(models.Model):
    filename = models.FileField('Filename', blank=True, null=True)
