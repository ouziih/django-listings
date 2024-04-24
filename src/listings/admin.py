from django.contrib import admin
from listings.models import Band, Vetements, Panier, Client


class BandAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    list_display = ('name', 'year_formed', 'genre', 'active', 'biography') # liste les champs que nous voulons sur l'affichage de la liste

class VetementsAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    list_display = ('name', 'prix', 'categorie')

class PanierAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    list_display = ('id_vetement','id_client', 'quantite')

class ClientAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    list_display = ('nom', 'email')

admin.site.register(Band, BandAdmin) # nous modifions cette ligne, en ajoutant un deuxième argument
admin.site.register(Vetements, VetementsAdmin)
admin.site.register(Panier, PanierAdmin)
admin.site.register(Client, ClientAdmin)