from datetime import datetime
from django.db import models
from django.utils import timezone
# Create your models here.

def getcohort():
    date = timezone.now()
    cohort = datetime.strftime(date,"%B-%Y")
    return(cohort)


class Student(models.Model):
    firstname = models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)
    cohort = models.CharField(default=getcohort, max_length=20,)
    date = models.DateField(auto_now=True)


    def __str__(self):
        return self.firstname



class Book(models.Model):
    title = models.CharField(max_length=100)
    no_of_pages = models.IntegerField()
    author = models.CharField(max_length=100)
    owner =models.ForeignKey(Student,on_delete=models.CASCADE)
    date = models.DateTimeField()


    def __str__(self):
        return self.title
