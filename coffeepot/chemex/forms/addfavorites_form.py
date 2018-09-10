from django import forms
from chemex.models import Roast



class FavoriteRoast(forms.ModelForm):

    class Meta:

        model = Roast
        fields = ('name', 'roaster', 'user',)


