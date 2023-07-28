import datetime
from django.db import models

# Create your models here.

# Widecity core user Model 
# Please be carefull while working with these files

class Users(models.Model):
    FirstName      =   models.CharField(max_length=50,default='None')
    LastName       =   models.CharField(max_length=50,default='None')
    Email           =   models.CharField(max_length=50,default='None')
    Password        =   models.CharField(max_length=50,default='None')
    RecoveryEmail  =   models.CharField(max_length=50,default='None')
    CountryCode  =   models.CharField(max_length=50,default='None')
    ContactNumber  =   models.CharField(max_length=50,default='None')
    City            =   models.CharField(max_length=50,default='None')
    Street          =   models.CharField(max_length=50,default='None')
    Country         =   models.CharField(max_length=50,default='None')
    Address1       =   models.CharField(max_length=50,default='None')
    Address2       =   models.CharField(max_length=50,default='None')
    Address3       =   models.CharField(max_length=50,default='None')
    Registered_On   =   models.CharField(max_length=50,default='None')
    
    def __str__(self) -> str:
        return self.Email
    
class User_Login_History(models.Model):
    Email           =   models.CharField(max_length=50,default='None')
    Date            =   models.CharField(max_length=50,default=datetime.date.today())
    Time            =   models.CharField(max_length=50,default=datetime.datetime.now().strftime('%H:%M:%S'))
    
    def __str__(self) -> str:
        return self.Email