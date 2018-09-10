from django.contrib import admin


from .models import CoffeeFarm, Roaster, Roast, BrewingMethod, CustomerBrewing, UserRoast, UserBrewingMethod, CoffeeShop


# Register your models here.
# admin.site.register(Customer)
admin.site.register(CoffeeFarm)
admin.site.register(Roaster)
admin.site.register(Roast)
admin.site.register(BrewingMethod)
admin.site.register(UserRoast)
admin.site.register(UserBrewingMethod)
admin.site.register(CustomerBrewing)
admin.site.register(CoffeeShop)

