from django.urls import path        # objeto path cria entrada e resposta
from . import views
urlpatterns = [ #lista de objetoss
 path('', views.natal), #objeto com dois parametros (vazio -> a VIEW que vai passar esse,  importando aquivo views e chamando função Natal)
 path('',views.tiradentes)
 
]