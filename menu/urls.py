from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('addfood', views.addFood, name='add-food'),
    path('editfood', views.editFood, name='edit-food'),
    path('update/food/<str:food>', views.updateFood, name='update-food'),
    path('runout/food/<str:food>', views.runoutFood, name='runout-food'),
    path('active/food/<str:food>', views.activeFood, name='active-food'),
    path('addfood/success', views.addFoodSuccess, name='add-food-suc'),
    path('adddrink', views.addDrink, name='add-drink'),
    path('editdrink', views.editDrink, name='edit-drink'),
    path('update/drink/<str:drink>', views.updateDrink, name='update-drink'),
    path('runout/drink/<str:drink>', views.runoutDrink, name='runout-drink'),
    path('active/drink/<str:drink>', views.activeDrink, name='active-drink'),
    path('adddrink/success', views.addDrinkSuccess, name='add-drink-suc'),
    path('itadakizen-london/foodmenu', views.foodMenu, name='food-menu'),
    path('itadakizen-london/drinkmenu', views.drinkMenu, name='drink-menu')
]
