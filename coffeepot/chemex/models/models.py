from django.db import models
from django.contrib.auth.models import User


# class Customer(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE,)
#     street = models.CharField(max_length=100, blank=True)
#     phone = models.CharField(max_length=20, blank=True)
#     city = models.CharField(max_length=100, blank=True)
#     state = models.CharField(max_length=2, blank=True)
#     zipcode = models.CharField(max_length=5, blank=True)


#     def __str__(self):

#         return f'{self.user.first_name} {self.user.last_name}'


class CoffeeFarm(models.Model):
    name = models.CharField(max_length=100, blank=True)

    def __str__(self):

        return self.name


class Roaster(models.Model):
    name = models.CharField(max_length=100, blank=True)
    street = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=2, blank=True)
    zipcode = models.CharField(max_length=5, blank=True)
    farm = models.ManyToManyField(CoffeeFarm)

    def __str__(self):

        return self.name


class Roast(models.Model):
    name = models.CharField(max_length=100, blank=True)
    roaster = models.ForeignKey(Roaster, on_delete=models.CASCADE, null=True)

    def __str__(self):

        return self.name


class BrewingMethod(models.Model):
    name = models.CharField(max_length=100, blank=True)

    def __str__(self):

        return self.name

class UserBrewingMethod(models.Model):
    """Joining table so customer can save their favorite brewing method on their profile
        Author: jacob smith
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    brewing_method = models.ForeignKey(BrewingMethod, on_delete=models.CASCADE, null=True)

    def __str__(self):

        return self.brewing_method

class UserRoast(models.Model):
    """Joining table so customer can save their favorite roast on their profile
        Author: jacob smith
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    roast = models.ForeignKey(Roast, on_delete=models.CASCADE, null=True)

    def __str__(self):

        return self.roast

class CustomerBrewing(models.Model):
    # Brew Calculator will need to add water and bloom amounts to model
    name = models.CharField(max_length=100, blank=True)
    date = models.DateField(max_length=100, auto_now=True)
    rating = models.CharField(max_length=5, blank=True)
    coffee = models.PositiveSmallIntegerField()
    bloom = models.PositiveSmallIntegerField(blank=True)
    water = models.PositiveSmallIntegerField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    method = models.ForeignKey(BrewingMethod, on_delete=models.CASCADE, null=True)
    roast = models.ForeignKey(Roast, on_delete=models.CASCADE, null=True)


    def __str__(self):

        return f'{self.name} was brewed on {self.date}'


class CoffeeShop(models.Model):
    name = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)


    def __str__(self):

        return f'{self.name} is located in {self.location}'

