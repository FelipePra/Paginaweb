from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .models import Manga
from .forms import MangaForm

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from .models import Manga
from .forms import MangaForm


def ingreso(request):
    if request.method == 'POST':
        form = MangaForm(request.POST, request.FILES)
        if form.is_valid():
            manga = form.save(commit=False)
            manga.save()
            messages.success(request, 'Manga ingresado con éxito!')
            return redirect('ingreso')
        else:
            messages.error(request, 'Error al ingresar el manga. Por favor, revise los datos ingresados.')
    else:
        form = MangaForm()
    
    return render(request, 'ingreso_manga.html', {'form': form})


def listado_mangas(request):
    mangas = Manga.objects.all()
    
    # Filtrar por tipo de manga
    manga_type_filter = request.GET.get('manga_type_filter', None)
    if manga_type_filter:
        mangas = mangas.filter(manga_type=manga_type_filter)
    
    return render(request, 'listado_mangas.html', {'mangas': mangas, 'manga_type_filter': manga_type_filter})


def detalle_manga(request, pk):
    manga = get_object_or_404(Manga, pk=pk)
    return render(request, '/detalle_manga.html', {'manga': manga})


def eliminar_manga(request, pk):
    manga = get_object_or_404(Manga, pk=pk)
    manga.delete()
    messages.success(request, 'Manga eliminado con éxito!')
    return redirect('listado_mangas')
