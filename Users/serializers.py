from rest_framework import serializers

from core.Users.models import Users

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['FirstName','LastName','Email','ContactNumber','RecoveryEmail','Registered_On']