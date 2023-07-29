import datetime
import re
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView

from .serializers import Userserializer

from .models import User_Login_History, Users
# Create your views here.

class Register(APIView):
    def post(self, request):
        try:
            # fetch the data from the request
            First_Name = request.data['First_Name']
            Last_Name = request.data['Last_Name']
            Email = request.data['Email']
            Country_Code = request.data['Country_Code']
            Contact_Number = request.data['Contact_Number']
            Password = request.data['Password']
        except Exception as e:
            return JsonResponse({'status':'failed','error':str(e)})
        
        # Validating the data
        # validating first name
        if len(First_Name)<1:
            return JsonResponse({'status':'failed','error':'First Name cannot be null'})
        # validating Last name
        if len(Last_Name)<1:
            return JsonResponse({'status':'failed','error':'Last Name cannot be null'})
        # Validate the email using regX
        if not re.fullmatch( r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b',Email):
            return JsonResponse({'status':'Wrong Email id'})
        
        # Password Validation
        # testng the length
        if not len(Password) >= 8:
            return JsonResponse({'status':'password should contain atleast 8 charecter'})
        # checking numbers in password
        if not re.search('[0-9]',Password):
            return JsonResponse({'status':'password should contain atleast one number'})
        # checking whether the password contain any capital letters
        if not re.search('[A-Z]',Password):
            return JsonResponse({'status':'password should contain atleast one Capital Letter'})
        # checking whether the password contain any small letters
        if not re.search('[a-z]',Password):
            return JsonResponse({'status':'password should contain atleast one small letter'})
        # validating contact number
        try:int(Contact_Number)
        except:return JsonResponse({'status':'contact number should contain only numbers'})

        # checking whether the user already have an account
        # A user can have multiple accounts in same contact number. not allowed to create multiple users in same email id
        if Users.objects.filter(Email=Email).exists():
            return JsonResponse({'status':'failed',"error":'email id already exist'})
        if Users.objects.filter(ContactNumber=Contact_Number).exists():
            pass
      
        New_User = Users.objects.create(FirstName=First_Name, LastName=Last_Name,CountryCode=Country_Code, ContactNumber=Contact_Number, Email=Email, Password=Password, Registered_On = datetime.date.today())
        New_User.save()
        return JsonResponse({'status':'success'})
        
class Login(APIView):
    def post(self,request):
        # fetching the login data from the request
        try:
            Email = request.data['Email']
            Password = request.data['Password']
        except:
            return JsonResponse({'status':'failed','error':'required Email, Password'})
        # validating the data
        # validating email
        if not  re.fullmatch( r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b',str(Email)):
            return JsonResponse({'status':'failed','error':'Invalid Email id'})
        
        # validating the password
        # testng the length
        if not len(Password) >= 8:
            return JsonResponse({'error':'password should contain atleast 8 charecter','status':'failed'})
        # checking numbers in password
        if not re.search('[0-9]',Password):
            return JsonResponse({'error':'password should contain atleast one number','status':'failed'})
        # checking whether the password contain any capital letters
        if not re.search('[A-Z]',Password):
            return JsonResponse({'error':'password should contain atleast one Capital Letter','status':'failed'})
        # checking whether the password contain any small letters
        if not re.search('[a-z]',Password):
            return JsonResponse({'error':'password should contain atleast one small letter','status':'failed'})
        
        # Checking for User with Email
        if not Users.objects.filter(Email=Email).exists():
            return JsonResponse({'status':'failed','error':'User Does not exist, create new account'})
        user = Users.objects.get(Email=Email)
        if not user.Password == Password:
            return JsonResponse({'status':'failed','error':'Wrong Password'})
        print('A USER LOGGED IN SUCCESSFULLY')
        # Saving login status in wdiecity user history
        User_Login_History.objects.create(Email=Email).save()
        
        
        return JsonResponse({'status':'success'})
    
    
class CheckEmail(APIView):
    def get(self,request,Email):
        if Users.objects.filter(Email=Email).exists():
            return JsonResponse({'status':'success'})
        else:
            return JsonResponse({'status':'failed'})    
        
class CheckContactNumber(APIView):
    def get(self,request,ContactNumber):
        if Users.objects.filter(ContactNumber=ContactNumber).exists():
            return JsonResponse({'status':'success'})
        else:
            return JsonResponse({'status':'failed'})      
          
class GetUser(APIView):
    def get(self,request,Email):
        if Users.objects.filter(Email=Email).exists():
            user = Users.objects.get(Email=Email)
            serializeduser = Userserializer(user,many=True)
            return JsonResponse({'status':'success','data':serializeduser.data})
        else:
            return JsonResponse({'status':'failed'})