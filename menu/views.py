from django.shortcuts import render, redirect
from .forms import *
from .models import *


# Create your views here.

def index(request):
    return render(request, 'menu/index.html')

def addFood(request):
    """
    this view add food item to db
    """
    title = "Add a new food item"
    action = "/addfood"
    if request.method == "POST":
        food_form = FoodMenuItemForm(data=request.POST)
        if food_form.is_valid():
            food_form.save()
            return redirect('/addfood/success')
    else:
        food_form = FoodMenuItemForm()

    return render(request, 'menu/add.html', {'form':food_form, 'title':title, 'action':action})


def editFood(request):
    food_menu = FoodMenuItem.objects.all().order_by('item_name')
    link = 'food'
    food_category = FoodMenuItem._meta.get_field('category').choices
    category = []
    for c in food_category:
        category.append(c[0])
    return render(request, "menu/edit.html", {'menu':food_menu, 'link':link, 'categories':category})

def updateFood(request, food):
    title = "Edit food item"
    link = "/update/food/" + food
    action = link
    food_menu = FoodMenuItem.objects.get(item_name=food)
    if request.method == "POST":
        food_form = FoodMenuItemForm(data=request.POST, instance=food_menu)
        if food_form.is_valid():
            food_form.save()
            return redirect('/addfood/success')
    else:
        food_form = FoodMenuItemForm(instance=food_menu)

    return render(request, 'menu/add.html', {'form':food_form, 'title':title, 'action':action})

def runoutFood(request, food):
    """
    runout button on food edit page
    """
    item = FoodMenuItem.objects.get(item_name=food)
    if item.runout == False:
        item.runout = True
        item.save()
    else:
        item.runout = False
        item.save()

    return redirect('/editfood')

def activeFood(request, food):
    """
    active button on food edit page
    """
    item = FoodMenuItem.objects.get(item_name=food)
    if item.active == False:
        item.active = True
        item.save()
    else:
        item.active = False
        item.save()

    return redirect('/editfood')

def addFoodSuccess(request):
    message = "Food item successfully saved 🙌🏼"
    link_add = "/addfood"
    link_edit = "/editfood"
    return render(request, 'menu/addSuccess.html', {'message':message, 'link_add':link_add, 'link_edit':link_edit})

def addDrink(request):
    """
    this view add drink item to db
    """
    title = "Add a new drink item"
    action = "/adddrink"
    if request.method == 'POST':
        drink_form = DrinkMenuItemForm(data=request.POST)
        if drink_form.is_valid():
            drink_form.save()
            return redirect('/adddrink/success')
    else:
        drink_form = DrinkMenuItemForm()

    return render(request, 'menu/add.html', {'form':drink_form, 'title':title, 'action':action})

def editDrink(request):
    drink_menu = DrinkMenuItem.objects.all().order_by('item_name')
    link = 'drink'
    drink_category = DrinkMenuItem._meta.get_field('category').choices
    category = []
    for c in drink_category:
        category.append(c[0])
    return render(request, "menu/edit.html", {'menu':drink_menu, 'link':link, 'categories':category})

def updateDrink(request, drink):
    title = "Edit drink item"
    link = "/update/drink/" + drink
    action = link
    drink_menu = DrinkMenuItem.objects.get(item_name=drink)
    if request.method == 'POST':
        drink_form = DrinkMenuItemForm(data=request.POST, instance=drink_menu)
        if drink_form.is_valid():
            drink_form.save()
            return redirect('/adddrink/success')
    else:
        drink_form = DrinkMenuItemForm(instance=drink_menu)

    return render(request, 'menu/add.html', {'form':drink_form, 'title':title, 'action':action})

def runoutDrink(request, drink):
    """
    runout button on food edit page
    """
    item = DrinkMenuItem.objects.get(item_name=drink)
    if item.runout == False:
        item.runout = True
        item.save()
    else:
        item.runout = False
        item.save()

    return redirect('/editdrink')

def activeDrink(request, drink):
    """
    active button on food edit page
    """
    item = DrinkMenuItem.objects.get(item_name=drink)
    if item.active == False:
        item.active = True
        item.save()
    else:
        item.active = False
        item.save()

    return redirect('/editdrink')

def addDrinkSuccess(request):
    message = "Drink item successfully saved 🙌🏼"
    link_add = "/adddrink"
    link_edit = "/editdrink"
    return render(request, 'menu/addSuccess.html', {'message':message, 'link_add':link_add, 'link_edit':link_edit})

def foodMenu(request):
    """
    this view diplay food menu for customer
    """
    food_menu = FoodMenuItem.objects.all()
    food_category = FoodMenuItem._meta.get_field('category').choices
    category = []
    for c in food_category:
        category.append(c[0])
    return render(request, 'menu/food.html', {'food_menu':food_menu, 'categories':category})

def drinkMenu(request):
    """
    this view dislay drink menu for customer
    """
    drink_menu = DrinkMenuItem.objects.all()
    drink_category = DrinkMenuItem._meta.get_field('category').choices
    category = []
    for c in drink_category:
        category.append(c[0])
    print(drink_menu[0].category)
    return render(request, 'menu/drink.html', {'drink_menu':drink_menu, 'categories':category})
