from rest_framework import serializers

from .models import Users

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['FirstName','LastName','Email','ContactNumber','RecoveryEmail','Registered_On']