from django import forms
from pokemon.models import Pokemon

# Form Pokemon
class PokemonForm(forms.ModelForm):
    class Meta:
        model= Pokemon
        fields='__all__'