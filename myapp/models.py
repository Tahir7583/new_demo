from django.db import models

# Create your models here.


class Recruiters(models.Model):
    gender=models.CharField(max_length=100)
    dob=models.DateField()
    phone=models.IntegerField()
    marital_status=models.CharField(max_length=100)
    home_town=models.CharField(max_length=100)
    pincode=models.IntegerField()
    curent_location=models.CharField(max_length=100)
    experince=models.IntegerField()
    language=models.CharField(max_length=100)
    
class Recruiter_Education(models.Model):
    recruiter_id=models.ManyToManyField(Recruiters,related_name='recruiter_id')
    degree=models.CharField(max_length=100)
    fields_of_specialization=models.CharField(max_length=100)
    institute_name=models.CharField(max_length=200)
    data_of_completion=models.DateField()