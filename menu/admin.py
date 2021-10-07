from django.contrib import admin
from .models import *

# Register your models here.

class FoodMenuItemAdmin(admin.ModelAdmin):
    list_display = ('item_name','category','description','price','active','runout','glueten_free','glueten_free_option','sesame','soybeans','nuts','peanuts','mustard')

class DrinkMenuItemAdmin(admin.ModelAdmin):
    list_display = ('item_name','category','description','price01', 'price02','price03','active','runout','sulpher')

admin.site.register(FoodMenuItem, FoodMenuItemAdmin)
admin.site.register(DrinkMenuItem, DrinkMenuItemAdmin)
