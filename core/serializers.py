from rest_framework import serializers
from .models import NewUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer




class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ('email', 'user_name','password',)
        extra_kwargs ={'password':{'write_only':True}}
        
    
    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        password = validated_data['password']    
        if password is not None:
            instance.set_password(validated_data['password'])
        instance.save()
        return instance

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.user_name
        # ...

        return token    