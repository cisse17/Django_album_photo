from django.shortcuts import render, redirect, get_object_or_404
from . models import Categorie, Photo
# Create your views here.

def galerie(request):
    categorie = request.GET.get('categorie')
    if categorie == None: #si la valeur categorie egale none on retourne ttes les categories c a d tte la galerie (les images ;  photos = Photo.objects.all())
        photos = Photo.objects.all()
           
    else:
        photos = Photo.objects.filter(categorie__name__contains=categorie)  #pr faire le tri des categories 

    categories = Categorie.objects.all()
    #photos = Photo.objects.all()
    context = {'categories': categories,
               'photos': photos}
    return render(request, 'photos/galerie.html', context)


def voirPhoto(request, pk):
    #pr voir la photo
    photo = Photo.objects.get(id=pk)
    return render(request, 'photos/photos.html', {'photo': photo})


def supprimer_photo(request, pk):
    obj = get_object_or_404(Photo, id=pk) #=> pareil mais la seule difference c l'affichage de la page d'erreur
    #photo = Photo.objects.get(id=pk)
    obj.delete()
    return redirect('galerie') 




def ajouterPhoto(request):
    categories = Categorie.objects.all()

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image') # name= 'image' 

        if data['categorie'] != 'none':
            categorie =Categorie.objects.get(id=data['categorie'])
        
        elif data['nouvelle_categorie'] != '':
            categorie, created = Categorie.objects.get_or_create(name=data['nouvelle_categorie'])
        else:
            categorie = None

        photo = Photo.objects.create(
            categorie=categorie,  #ds le model on a crée la relation
            description=data['description'],
            image=image, 
        )

        return redirect('galerie') 
       
    context = {'categories': categories}

    return render(request, 'photos/ajouter.html', context)


