from django import forms
from .models import *
from django.forms import ModelForm

FOOD_CATEGORY_CHOICES = [
    ('TAPAS', 'Tapas'),
    ('DESERT', 'Desert'),
    ('SPECIAL', 'Special')
]

DRINK_CATEGORY_CHOICES = [
    ('SOFT DRINK', 'Soft drink'),
    ('HOT DRINK', 'Hot drink'),
    ('BEER', 'Beer'),
    ('WHITE WINE', 'White wine'),
    ('RED WINE', 'Red wine'),
    ('COCKTAIL', 'Cocktail'),
    ('SAKE', 'Sake'),
    ('OTHER', 'Other'),
    ('SPECIAL', 'Special')
]

class FoodMenuItemForm(forms.ModelForm):
    item_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'name', 'class':'menu-form'}))
    description = forms.CharField(label='',
    widget=forms.Textarea(attrs={'placeholder':'description', 'class':'menu-form'}), required=False)
    category = forms.ChoiceField(label='category', choices=FOOD_CATEGORY_CHOICES, widget=forms.Select(attrs={'placeholder':'category', 'class':'menu-form'}))
    price = forms.DecimalField(label="price", widget=forms.NumberInput(attrs={'placeholder':'£', 'class':'menu-form'}))
    active = forms.NullBooleanField(label='active', widget=forms.Select(choices=[(True,'yes'),(False,'no')]))
    runout = forms.NullBooleanField(label='run-out', widget=forms.Select(choices=[(False,'no'),(True,'yes')]))
    glueten_free = forms.NullBooleanField(label='glueten free', widget=forms.Select(choices=[(False,'no'),(True,'yes')]))
    glueten_free_option = forms.NullBooleanField(label='glueten free option availble', widget=forms.Select(choices=[(False,'no'),(True,'yes')]))
    onion_garlic_free_option = forms.NullBooleanField(label='glueten free option availble', widget=forms.Select(choices=[(False,'no'),(True,'yes')]))
    sesame = forms.NullBooleanField(label='contain sesame',widget=forms.Select(choices=[(False,'no'),(True,'yes')]))
    soybeans = forms.NullBooleanField(label='contain soybeans',widget=forms.Select(choices=[(False,'no'),(True,'yes')]))
    nuts = forms.NullBooleanField(label='contain nuts',widget=forms.Select(choices=[(False,'no'),(True,'yes')]))
    peanuts = forms.NullBooleanField(label='contain peanuts',widget=forms.Select(choices=[(False,'no'),(True,'yes')]))
    mustard = forms.NullBooleanField(label='contain mustard',widget=forms.Select(choices=[(False,'no'),(True,'yes')]))

    class Meta:
        model = FoodMenuItem
        fields = ('item_name', 'description', 'category','price','active','runout','glueten_free','glueten_free_option','onion_garlic_free_option', 'sesame','soybeans','nuts','peanuts', 'mustard')


class DrinkMenuItemForm(forms.ModelForm):
    item_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'name', 'class':'menu-form'}))
    description = forms.CharField(label='',
    widget=forms.Textarea(attrs={'placeholder':'description', 'class':'menu-form'}), required=False)
    category = forms.ChoiceField(label='category', choices=DRINK_CATEGORY_CHOICES, widget=forms.Select( attrs={'placeholder':'category', 'class':'menu-form'}))
    price01 = forms.DecimalField(label="price", widget=forms.NumberInput(attrs={'placeholder':'£', 'class':'menu-form'}))
    price02 = forms.DecimalField(label="price", widget=forms.NumberInput(attrs={'placeholder':'£', 'class':'menu-form'}), required=False)
    price03 = forms.DecimalField(label="price", widget=forms.NumberInput(attrs={'placeholder':'£', 'class':'menu-form'}), required=False)
    active = forms.NullBooleanField(label='active',widget=forms.Select(choices=[(True,'yes'),(False,'no')]))
    runout = forms.NullBooleanField(label='run-out',widget=forms.Select(choices=[(False,'no'),(True,'yes')]))
    sulpher = forms.NullBooleanField(label='contain any sulphur dioxide and sulphite',widget=forms.Select(choices=[(False,'no'),(True,'yes')]))

    class Meta:
        model = DrinkMenuItem
        fields = ('item_name','description','category','price01','price02','price03','active','runout','sulpher')
