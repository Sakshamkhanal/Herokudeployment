from django.urls import include, path
from knox import views as knox_views
from rest_framework import routers

from dsorders.api.ViewSets import *

from . import views

router = routers.DefaultRouter()
router.register(r'dealer',DealerViewSet,basename='dealer')
router.register(r'salesman',SalesmanViewSet,basename='salesman')
router.register(r'items',ItemsViewSet,basename='items')
router.register(r'order',OrderViewset,basename='order')
router.register(r'shop',ShopViewSet,basename='shop')


urlpatterns = [
path('login/',views.login_api),
#path('login/',views.LoginView.as_view()),
path('user/',views.get_user_data),
path('register/',views.register_api),
path('logout/',knox_views.LogoutView.as_view()),
path('logoutall/',knox_views.LogoutAllView.as_view()),
path('api/',include(router.urls)),
]
