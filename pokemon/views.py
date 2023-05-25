from django.shortcuts import render, redirect
from models import Pokemon
from pokemon.forms import PokemonForm
# Create your views here.

def home(request):
    return render(request,"pokemon/home.html", {"pokemons":Pokemon.objects.all().values()})

def pokemon_create(request):
    if request.method == 'POST':
        form = PokemonForm(request.POST)
        if form.is_valid():
            pokemon= form.save()
            return redirect('home')
        else :
            form=PokemonForm()
    return render(request,"pokemon/home.html", {"pokemons":Pokemon.objects.all().values()})