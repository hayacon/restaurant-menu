from django.db import models

class FoodMenuItem(models.Model):
    item_name = models.CharField(max_length=100, null=False, blank=False, primary_key=True)
    CATEGORY_CHOICES = [
        ('TAPAS', 'Tapas'),
        ('DESERT', 'Desert'),
        ('SPECIAL', 'Special')
    ]
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, null=False, blank=False)
    description = models.CharField(max_length=500, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False)
    active = models.BooleanField(default=True)
    runout = models.BooleanField(default=False)
    glueten_free = models.BooleanField(default=False)
    glueten_free_option = models.BooleanField(default=False)
    onion_garlic_free_option = models.BooleanField(default=False)
    sesame = models.BooleanField(default=False)
    soybeans = models.BooleanField(default=False)
    nuts = models.BooleanField(default=False)
    peanuts = models.BooleanField(default=False)
    mustard = models.BooleanField(default=False)

class DrinkMenuItem(models.Model):
    item_name = models.CharField(max_length=100, null=False, blank=False, primary_key=True)
    CATEGORY_CHOICES = [
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
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, null=False, blank=False)
    description = models.CharField(max_length=500, null=True, blank=True)
    price01 = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False)
    price02 = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    price03 = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    active = models.BooleanField(default=True)
    runout = models.BooleanField(default=False)
    sulpher = models.BooleanField(default=False)
