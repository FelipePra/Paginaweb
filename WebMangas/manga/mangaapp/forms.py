from django import forms
from .models import Manga


class MangaForm(forms.ModelForm):
    class Meta:
        model = Manga
        fields = ['nombre', 'autor', 'genero', 'demografia', 'cantidad_capitulos', 'sinopsis', 'tipo']

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if len(nombre) < 3:
            raise forms.ValidationError('El nombre debe tener al menos 3 caracteres')
        return nombre

    def clean_sinopsis(self):
        sinopsis = self.cleaned_data.get('sinopsis')
        if len(sinopsis) < 20:
            raise forms.ValidationError('La sinopsis debe tener al menos 20 caracteres')
        return sinopsis
