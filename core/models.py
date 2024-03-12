from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=15)
    people = models.CharField(max_length=20)

    class Meta:
        db_table = 'core_user_1'


class Wine(models.Model):
    username = models.CharField(max_length=20)
    age = models.CharField(max_length=20)
    sex = models.CharField(max_length=20)
    cp = models.CharField(max_length=20)
    trestbps = models.CharField(max_length=20)
    chol = models.CharField(max_length=20)
    fbs = models.CharField(max_length=20)
    restecg = models.CharField(max_length=20)
    thalach = models.CharField(max_length=20)
    exang = models.CharField(max_length=20)
    oldpeak = models.CharField(max_length=20)
    slope = models.CharField(max_length=20)
    ca = models.CharField(max_length=20)
    thal = models.CharField(max_length=20)
    target = models.CharField(max_length=20)

    class Meta:
        db_table = 'core_wine_1'
