from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView

from Users.models import Users

from .serializers import UserProductserializer, all_products_serializer
from .models import All_Products, UserProducts
# Create your views here.

class GetAllProducts(APIView):
    def get(self,request):
        all_products = All_Products.objects.all()
        serialized = all_products_serializer(all_products,many=True)
        return JsonResponse({'status':'success','data':serialized.data})
    
class UploadProduct(APIView):
    def post(self,request):
        try:
            Name = request.data['Name']
            Icon = request.data['Icon']
            ImageA = request.data['ImageA']
            ImageB = request.data['ImageB']
            ImageC = request.data['ImageC']
            ImageD = request.data['ImageD']
            Description = request.data['Description']
            DownloadLink = request.data['DownloadLink']
        except:
            return JsonResponse({'status':'failed','error':'required Name, Icon, ImageA, ImageB, ImageC,ImageD, Description, DownloadLink'})
        try:
            # validating the fields
            # validatin the Product Name
            if len(Name) <1:
                return JsonResponse({'status':'failed','error':'Name cannot be empty'})     
            if All_Products.objects.filter(Name=Name).exists():
                return JsonResponse({'status':'failed','error':'Product with this name already exist'})     
            if not Icon:
                return JsonResponse({'status':'failed','error':'Icon field cannot be null'})    
            if not ImageA:
                return JsonResponse({'status':'failed','error':'ImageA field cannot be null'})    
            if not ImageB:
                return JsonResponse({'status':'failed','error':'ImageB field cannot be null'})    
            if not ImageC:
                return JsonResponse({'status':'failed','error':'ImageC field cannot be null'})    
            if not ImageD:
                return JsonResponse({'status':'failed','error':'ImageD field cannot be null'})
            if len(Description) <50:
                return JsonResponse({'status':'failed','error':'Description should have atleast 50 charecters'}) 
            if len(DownloadLink) <1:
                return JsonResponse({'status':'failed','error':'DownloadLink cannot be empty'}) 
        except:
            return JsonResponse({'status':'failed','error':'Something went wrong with the validation features, please contact the developers'})
        try:
            newProduct = All_Products.objects.create(Name=Name,Icon=Icon,ImageA=ImageA,ImageB=ImageB,ImageC=ImageC,ImageD=ImageD,Description=Description,DownloadLink=DownloadLink)
            newProduct.save()
        except Exception as e:
            return JsonResponse({'status':'failed','error':str(e)})
        return JsonResponse({'status':'success'})
    
    
class HandleUserProducts(APIView):
    def get(self,request,Email):
        if Users.objects.filter(Email=Email).exists():  
            if UserProducts.objects.filter(UserEmail=Email).exists():
                products =  UserProducts.objects.filter(UserEmail=Email)
                userproductSerialized = UserProductserializer(products,many=True)
                return JsonResponse({'status':'success','data':userproductSerialized.data})
        return JsonResponse({'status':'failed','reason':'email id does not exist or no products'})
    def put(self,request):
        try:
            UserEmail = request.data['UserEmail']
            ProductName = request.data['ProductName']
            DueDate = request.data['DueDate']
        except:
            return JsonResponse({'status':'failed'})
        try:
            userproduct = UserProducts.objects.get(UserEmail=UserEmail,ProductName=ProductName)
            userproduct.DueDate = DueDate
            userproduct.save()
            return JsonResponse({'status':'success'})
        except:
            return JsonResponse({'status':'failed'})
    def post(self,request):
        try:
            UserEmail = request.data['UserEmail']
            ProductName = request.data['ProductName']
            DueDate = request.data['DueDate']
            if Users.objects.filter(Email=UserEmail).exists():
                return JsonResponse({'status':'failed','error':'user not found'})
            if UserProducts.objects.filter(UserEmail=UserEmail,ProductName=ProductName).exists():
                return JsonResponse({'status':'failed','error':'Product already added'})
        except:
            return JsonResponse({'status':'failed'})
        try:
            UserProducts.objects.create(UserEmail=UserEmail,ProductName=ProductName,DueDate=DueDate).save()
            return JsonResponse({'status':'success'})
        except:
            return JsonResponse({'status':'failed'})