from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Pokemon(models.Model):
    class Type(models.TextChoices):
        Feu = "feu"
        Electric = "elec"
        Eau = "eau"
        Feuille = "feuille"
        Normal = "normal"
        Sol= "sol"
        Roche = "roche"
        Insect = "insect"
        Glace = "glace"
        Acier = "acier"
        Psy= 'psy'
        Spectre= "spectre"
        Dragon = "dragon"
        Normale = "normale"
        Tenebre= "ténébre"
    nom=models.CharField(max_length=100
    )
    type=models.CharField(choices=Type.choices, max_length=10)
    niveau=models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(99)]
    )