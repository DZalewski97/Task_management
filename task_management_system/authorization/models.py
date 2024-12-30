from django.db import models

class People(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=20)
    task = models.CharField(max_length=300)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.name

# Create your models here.
