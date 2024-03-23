from django.shortcuts import render, get_object_or_404, redirect
from .models import Post  # Importa el modelo Post del archivo models.py en el mismo directorio
from django.utils import timezone  # Importa la función timezone para trabajar con fechas y horas
from .forms import PostForm


def post_list(request):
    return render(request, 'blog/post_list.html', {})

#"Renderizar" en el contexto de desarrollo web significa tomar una plantilla (que es básicamente un archivo HTML con marcadores especiales para insertar datos dinámicos) y procesarla para producir un resultado final que se puede enviar al navegador web para ser mostrado al usuario. En el caso de Django, la función render toma una solicitud del usuario, una plantilla y un diccionario de datos (opcional) y devuelve una respuesta HTTP que contiene el resultado de procesar la plantilla con los datos proporcionados. Entonces, en el código que mencionaste, render se utiliza para crear la respuesta que mostrará los posts recuperados en la plantilla blog/post_list.html.

def post_list(request):
    # Recupera todos los posts cuya fecha de publicación es anterior o igual a la fecha y hora actuales
    # y los ordena por fecha de publicación en orden ascendente
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # Renderiza la plantilla 'blog/post_list.html' con los posts recuperados
    # Además, pasa un diccionario como contexto con la clave 'posts' que contiene los posts recuperados
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})