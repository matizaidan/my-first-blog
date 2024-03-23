from django.urls import path  #funcion path, para definir las rutas URL en una aplicacion django.
from . import views # (.) -> representa el directorio actual, importa todas las vistas.

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]
