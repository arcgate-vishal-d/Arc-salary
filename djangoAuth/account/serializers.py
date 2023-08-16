
# from rest_framework import serializers

# from .models import User 

# class UserRegistrationSerializer(serializers.ModelSerializer):
    
#     password2 = serializers.CharField(style={"input_type":"password"}, write_only=True)
    
#     class Meta:
#         model = User
#         fields = ["email", "name", "password", "password2", "tc"]
        
#         extra_kwargs = {
#             "password": {"write_only":True},
#         }
        
#     def validate(self, data):
        
#         # password = self.data['password']
#         # password2 = self.data['password2']
        
#         password = data.get('password')
#         password2 = data.get('password2')
        
#         if password != password2:
#             raise serializers.ValidationError("Password is not matching!...")
#         return data
    
#     def create(self, validated_data):
#         return User.objects.create(**validated_data)
        
        
        
    
from rest_framework import serializers
from account.models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = User
        fields=['email','name','tc','password','password2']
        extra_kwargs={
            'password':{'write_only':True}
        }

    def validate(self, attrs):
        password=attrs.get('password')
        password2=attrs.pop('password2')
        if password != password2:
            raise serializers.ValidationError("Password and Confirm Password Does not match")
        return attrs

    def create(self, validate_data):
        return User.objects.create_user(**validate_data)