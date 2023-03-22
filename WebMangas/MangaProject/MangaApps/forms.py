from dataclasses import fields
from tkinter import Button
from django import forms

from MangaApps.models import Manga

class FormPersona(forms.ModelForm):
    class Meta:
        model = Manga
        fields = ['nombre','demografia','autor','genero','link','sinopsis','volumenes','capitulos','categoria','observacion']
    eCivil=[('casado','casad@'),('soltero','solter@'),('viudo','viud@'),('separado','separad@')]
    #id = forms.IntegerField()
    nombre = forms.CharField()
    fono = forms.CharField()
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    direccion = forms.CharField()
    email = forms.CharField()
    estado_civil = forms.CharField(widget=forms.Select (choices=eCivil))
    observacion = forms.CharField(widget=forms.Textarea(attrs={'rows':'2','class':'form-control'}))
    #estado = forms.CharField()
    

    fono.widget.attrs['class'] = 'form-control'
    nombre.widget.attrs['class'] = 'form-control'
    direccion.widget.attrs['class'] = 'form-control'
