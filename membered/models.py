from django.db import models
from django.utils import timezone

class Details(models.Model):
    Surname = models.TextField()
    Name = models.TextField()
    Address = models.TextField()
    Date_of_birth = models.DateTimeField()
    Age = models.IntegerField()
    Telephone = models.IntegerField()
    WhatsApp = models.IntegerField()
    Email = models.EmailField()
    Nationality = models.TextField()
    Sate_of_Origin = models.TextField()
    Session = models.TextField()
    Past_Qualification = models.TextField()
    Computer_Course = models.TextField()
    date = models.DateField()
    
class API(models.Model):
    Pk = models.IntegerField(unique = True, primary_key = True)
    Name = models.TextField()
    Department = models.TextField()

# Create your models here.
class David(models.Model):
    Name = models.TextField()
    Age = models.IntegerField()
    Date_Of_Birth = models.DateField()
    