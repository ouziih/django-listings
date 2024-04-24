from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django import forms

class Band(models.Model):

    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'

    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=10)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2024)])
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


class Vetements(models.Model):
    class Categories(models.TextChoices):
        HOMME = 'Homme'
        FEMME = 'Femme'
        
    categorie = models.fields.CharField(choices=Categories.choices, max_length=50)
    name = models.fields.CharField(max_length=100)
    prix = models.fields.IntegerField()
 
    def __str__(self):
        return f'{self.name}'


class Client(models.Model):
    nom = models.fields.CharField(max_length=100)
    email = models.fields.EmailField()

    def __str__(self):
        return f'{self.nom}'
    

class Panier(models.Model):
    id_vetement = models.ForeignKey(Vetements, null=True, on_delete=models.SET_NULL)
    id_client = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)
    quantite = models.fields.IntegerField()

    def __str__(self):
        return f'{self.id_vetement}'
    

class ContactUsForm(forms.Form):
   name = forms.CharField(required=False)
   email = forms.EmailField()
   message = forms.CharField(max_length=1000)


class VetementsForm(forms.ModelForm):
   class Meta:
     model = Vetements
     fields = '__all__'