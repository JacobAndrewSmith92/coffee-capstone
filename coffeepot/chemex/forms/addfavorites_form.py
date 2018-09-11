from django import forms
from chemex.models import Roast, Roaster, BrewingMethod



class FavoriteRoast(forms.ModelForm):

    class Meta:
        model = Roast
        fields = ('name', 'roaster',)

class FavoriteRoaster(forms.ModelForm):

    class Meta:
        model = Roaster
        fields = ('name', 'street', 'phone', 'city', 'state', 'zipcode')

class FavoriteBrewingMethod(forms.ModelForm):

    class Meta:
        model = BrewingMethod
        fields = ('name',)

    




