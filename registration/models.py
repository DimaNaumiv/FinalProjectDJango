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


class Result(models.Model):
    # Зв'язок багатьох результатів до одного юзера
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='results')
    
    group_type = models.CharField(max_length=40)
    qustion = models.CharField(max_length=100) # примітка: тут оддрук у слові question, але залишено як у вас
    answer = models.CharField(max_length=100)
    time = models.CharField(max_length=15)
    fails = models.CharField(max_length=20)
    min_const = models.CharField(max_length=20)
    max_const = models.CharField(max_length=20)