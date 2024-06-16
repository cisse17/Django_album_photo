from django.db import models

# Create your models here.
class Categorie(models.Model):
    name= models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.name
    

class Photo(models.Model):
    #je fais categorie pr faie le lien avk description ou image    delete
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True,  blank=True)
    image = models.ImageField(null=False, blank=False)
    description= models.TextField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.description



#cissebassirou.pythonanywhere.com
#/home/cissebassirou/photoshare
# mkvirtualenv --python=/usr/bin/python3.9  galerie-virtualenv


#jobs@acted.org
