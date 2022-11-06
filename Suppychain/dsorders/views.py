#view.py
from urllib import request

from django.contrib.auth import login
from knox.auth import AuthToken
from knox.views import LoginView as KnoxLoginView
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

from dsorders.api.serializers import RegisterSerializers


@api_view(['POST'])
def login_api(request):
	serializer=AuthTokenSerializer(data=request.data)
	serializer.is_valid(raise_exception=True)
	user = serializer.validated_data['user']
	_,token = AuthToken.objects.create(user)

	return Response({
	'user_info':{
		'id':user.id,
		'username':user.username,
		'email':user.email,
	},
	'token':token
	})

# class LoginView(KnoxLoginView):

# 	def post(self,request,format=None):
# 		serializer = AuthTokenSerializer(data=request.data)
# 		serializer.is_valid(raise_exception=True)
# 		user = serializer.validated_data['user']
# 		login(request,user)
# 		return super(LoginView,self).post(request,format=None)



@api_view(['POST'])
def register_api(request):
	serializer = RegisterSerializers(data=request.data)
	serializer.is_valid(raise_exception=True)

	user = serializer.save()
	_,token = AuthToken.objects.create(user)
	
	return Response({
	'user_info':{
		'id':user.id,
		'username':user.username,
		'email':user.email,
	},
	'token':token
	})



@api_view(['GET'])
def get_user_data(request):
    user = request.user

    if user.is_authenticated:
        return Response({
            'user_info':{
				'id':user.id,
				'username':user.username,
				'email':user.email,
				}
        })
    return Response({'error':'not is_authenticated'},status=400)

