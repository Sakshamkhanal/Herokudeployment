import email
from dsorders.models import Dealer, Item, Order, Salesman, Shop, User
from rest_framework import serializers, validators
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password

class RegisterSerializers(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['username','password','email','first_name','last_name']

		extra_kwargs ={
		"password":{"write_only":True},
		# "email":{
		# "required":True,
		# "allow_blank":False,
		# "validators":[
		# validators.UniqueValidator(
		# 			User.objects.all(),"A user with that Email already exists"
		# )
		# ]
		# }
		}

		def create(self,validated_data):
			username = validated_data.get('username')
			password = validated_data.get('password')
			email = validated_data.get('email')
			first_name = validated_data.get('first_name')
			last_name = validated_data.get('last_name')
		
			user = User.objects.create_user(
					username,
					'',
		    	#		password,
				#	email=email,
				#	first_name=first_name,
				#	last_name=last_name,
			)
			user.set_password(validated_data[password])
			user.save()
			return user



class DealerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dealer
        fields = ("__all__")
class SalesmanSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Salesman
        fields = ("__all__")

class ItemSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ("__all__")

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("__all__")

            
class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields =("__all__")

