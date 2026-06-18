from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)

    hash_password = models.CharField(max_length=200)

    created_at = models.DateField()
    updated_at = models.DateField()


class Session(models.Model):
    session_code = models.CharField(max_length=16, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sessions')

    created_at = models.DateField()
    updated_at = models.DateField()