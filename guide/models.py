from django.db import models

# Create your models here.
class Guide(models.Model):
    title = models.CharField(max_length=40)
    discription = models.CharField(max_length=100)
    group_type = models.CharField(max_length=40)

    created_by = models.CharField(max_length=40)
    created_at = models.DateField()

    changed_by = models.CharField(max_length=40)
    changed_at = models.DateField()
    
class Moduls(models.Model):
    guide = models.ForeignKey(Guide, on_delete=models.CASCADE, related_name='modules',null=True,blank=True)
    title = models.CharField(max_length=40)
    discription = models.CharField(max_length=100)
    text = models.CharField(max_length=500)

    created_by = models.CharField(max_length=40)
    created_at = models.DateField()

    changed_by = models.CharField(max_length=40)
    changed_at = models.DateField()
