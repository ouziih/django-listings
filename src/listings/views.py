# ~/projects/django-web-app/merchex/listings/views.py

from django.shortcuts import render
from listings.models import Band, Vetements, ContactUsForm, VetementsForm
from django.core.mail import send_mail
from django.shortcuts import redirect



def hello(request):
    list_vetement = Vetements.objects.all()
    return render(request, 'listings/hello.html', {'list_vetement' : list_vetement})

def about(request):
    return render(request, 'listings/about-us.html')

def annonce(request):
    list_vetement = Vetements.objects.all()
    return render(request, 'listings/annonce.html' , {'list_vetement' : list_vetement})

def details_produit(request, id):  
   vetement = Vetements.objects.get(id=id)
   return render(request,
          'listings/details_produit.html',
         {'vetement': vetement}) 

def contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
            subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=['admin@merchex.xyz'],
        )
        return redirect('contact')

    else:
        form = ContactUsForm()
    return render(request, 'listings/contact.html', {'form': form})

def blog(request):
    return render(request, 'listings/blog.html')

def panier(request):
    if request.method == 'POST':
        form = VetementsForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            band = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('details_vetement', band.id)

    else:
        form = VetementsForm()

    return render(request, 'listings/panier.html', {'form': form})