from django.shortcuts import render
from .models import Manga
from .forms import MangaForm

def agregar_manga(request):
    if request.method == 'POST':
        form = MangaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = MangaForm()
    return render(request, 'mangas/agregar_manga.html', {'form': form})
