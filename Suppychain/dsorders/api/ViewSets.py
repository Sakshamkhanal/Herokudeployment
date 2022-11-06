from multiprocessing import context
from sys import api_version
from urllib import request

from django.shortcuts import get_object_or_404
from dsorders.api.serializers import (DealerSerializer, ItemSerilizer,
                                      OrderSerializer, SalesmanSerilizer,
                                      ShopSerializer)
from dsorders.models import Dealer, Item, Order, Salesman, Shop
from html5lib import serialize
from knox.auth import AuthToken
from rest_framework import generics, permissions, status
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_api_key.permissions import HasAPIKey


#Models viewsets
class DealerViewSet(ModelViewSet):
   # permission_classes = (permissions.IsAuthenticated)
    serializer_class = DealerSerializer
    http_method_names = ['get']

    def get_queryset(self):
        queryset = Dealer.objects.all()
        return queryset


class SalesmanViewSet(ModelViewSet):
   # permission_classes = (permissions.IsAuthenticated)
    serializer_class = SalesmanSerilizer
    http_method_names = ['get', 'post']

    def get_queryset(self):
        query_set = Salesman.objects.filter(id=self.request.user.Salesman_user.id)

        return query_set

class ItemsViewSet(ModelViewSet):
    #permission_classes = (permissions.IsAuthenticated)
    serializer_class = ItemSerilizer

    http_method_names = ['get', 'post',]

    def get_queryset(self):
        query_set =  Item.objects.filter(id=self.request.user.Salesman_user.id)
        return query_set
        
class OrderViewset(ModelViewSet):
    #permission_classes = (permissions.IsAuthenticated)
    serializer_class = OrderSerializer

    http_method_names = ['get', 'post',]

    def get_queryset(self):
        query_set = Order.objects.filter(id=self.request.user.Salesman_user.id)
        return query_set


class ShopViewSet(ModelViewSet):
    #permission_classes = (permissions.IsAuthenticated)
    serializer_class = ShopSerializer

    http_method_names = ['get', 'post',]
    
    def get_queryset(self):
        query_set = Shop.objects.filter(id=self.request.user.Salesman_user.id)
        return query_set

