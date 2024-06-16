from django.urls import path
from .import views

urlpatterns = [
    path('', views.galerie, name="galerie"),
    path('photo/<str:pk>/', views.voirPhoto, name="photo"),
    path('supprimer_photo/<str:pk>/', views.supprimer_photo, name="supprimer_photo"),
    path('ajouter_photo/', views.ajouterPhoto, name="ajouter_photo"),
]