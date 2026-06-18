from django.db import models

# Create your models here.
class Major(models.Model):
    title = models.CharField(max_length=40)
    discription = models.CharField(max_length=80)
    group_type = models.CharField(max_length=40)

    created_by = models.CharField(max_length=40)
    created_at = models.DateField()

    changed_by = models.CharField(max_length=40)
    changed_at = models.DateField();