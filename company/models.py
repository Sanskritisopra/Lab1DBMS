from django.db import models

# Create your models here.
class XYZCompany(models.Model):
    InternID = models.IntegerField(primary_key=True)
    FirstName= models.CharField('First Name',max_length=255,default=None)
    LastName = models.CharField('Last Name',max_length=255,null=True,blank=True)
    TeamID = models.IntegerField()
    JoiningDate = models.DateField()
    ManagerID = models.BigIntegerField()
    Location = models.CharField(max_length=255)
    Stipend = models.IntegerField()
    PhoneNo = models.BigIntegerField()
    Email = models.EmailField()
    
    