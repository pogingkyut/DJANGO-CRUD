from django.db import models

class Person(models.Model):
    name= models.CharField(max_length=50, blank=False, null=False)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, blank=False, null=False)

    def __str__(self):
        return self.name