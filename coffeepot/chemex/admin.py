from django.contrib import admin


from .models import Customer, CoffeeFarm, Roaster, Roast, BrewingMethod, CustomerBrewing, CustomerRoast, CoffeeShop


# Register your models here.
admin.site.register(Customer)
admin.site.register(CoffeeFarm)
admin.site.register(Roaster)
admin.site.register(Roast)
admin.site.register(BrewingMethod)
admin.site.register(CustomerRoast)
admin.site.register(CustomerBrewing)
admin.site.register(CoffeeShop)

