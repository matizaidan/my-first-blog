from django.urls import path  #funcion path, para definir las rutas URL en una aplicacion django.
from . import views # (.) -> representa el directorio actual, importa todas las vistas.

urlpatterns = [
    path('', views.post_list, name='post_list'),
]

