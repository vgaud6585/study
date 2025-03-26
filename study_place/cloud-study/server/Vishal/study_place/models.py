from django.db import models

# Create your models here.
class User(models.Model):
  usr_age = models.IntegerField()
  usr_image = models.ImageField(upload_to='images/')


class StudyRecords(models.Model):
  usr_head = models.CharField(max_length=100)
  usr_heading = models.CharField(max_length=100)
  usr_description = models.CharField(max_length=100)
  usr_code_box = models.CharField(max_length=1000)
  usr_filearc = models.FileField(upload_to="store/")
  
  def __str__(self):
    return self.usr_heading
    
class spass(models.Model):
  usr_name = models.CharField(max_length=100)
  usr_pass = models.CharField(max_length=100)
  def __str__(self):
    return self.usr_name
  