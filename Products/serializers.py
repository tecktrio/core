from rest_framework import serializers

from .models import All_Products, UserProducts

class all_products_serializer(serializers.ModelSerializer):
    class Meta:
        model = All_Products
        fields = '__all__'
        
class UserProductserializer(serializers.ModelSerializer):
    class Meta:
        model = UserProducts
        fields = "__all__"
        