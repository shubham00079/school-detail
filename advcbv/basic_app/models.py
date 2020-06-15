from django.db import models
from django.urls import reverse
# Create your models here.

class School(models.Model):
    name = models.CharField(max_length = 40)
    principal = models.CharField(max_length = 40)
    location = models.CharField(max_length = 40)

    def  __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("basic_app:detail",kwargs={'pk':self.pk})


class Student(models.Model):
    name = models.CharField(max_length = 40)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
