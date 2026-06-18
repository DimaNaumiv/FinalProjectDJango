from django.db import models

# Create your models here.


class Pattern(models.Model):
    type = models.CharField(max_length=20)
    group_type = models.CharField(max_length=40)
    difficulty = models.IntegerField(null=True)
    value = models.CharField(max_length=100)
    ignorance = models.IntegerField(null=True)

    created_by = models.CharField(max_length=40)
    created_at = models.DateField()

    changed_by = models.CharField(max_length=40)
    changed_at = models.DateField()
