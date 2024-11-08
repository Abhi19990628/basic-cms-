from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField() 
    mobile_no = models.BigIntegerField() 
    address = models.TextField()

    def __str__(self):
        return self.name
