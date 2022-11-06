from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from .models import *
# Register your models here.
admin.site.register(Dealer)
admin.site.register(Salesman)
admin.site.register(Order)
admin.site.register(Item)
admin.site.register(User,UserAdmin)
admin.site.register(Shop)
