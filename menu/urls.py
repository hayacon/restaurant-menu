from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('addfood', views.addFood, name='add-food'),
    path('editfood', views.editFood, name='edit-food'),
    path('update/food/<str:food>', views.updateFood, name='update-food'),
    path('addfood/success', views.addFoodSuccess, name='add-food-suc'),
    path('adddrink', views.addDrink, name='add-drink'),
    path('editdrink', views.editDrink, name='edit-drink'),
    path('update/drink/<str:drink>', views.updateDrink, name='update-drink'),
    path('adddrink/success', views.addDrinkSuccess, name='add-drink-suc'),
    path('itadakizen/foodmenu', views.foodMenu, name='food-menu'),
    path('itadakizen/drinkmenu', views.drinkMenu, name='drink-menu')
]
