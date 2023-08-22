from typing import Any, Dict, Mapping, Optional, Type, Union
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import Laboratorio, DirectorGeneral, Producto

class LaboratorioForm(forms.ModelForm):
    class Meta:
        model = Laboratorio
        exclude = []
    
    def __init__(self, *args, **kwargs):
        super(LaboratorioForm, self).__init__(*args, **kwargs)
        self.fields['ciudad'].widget.attrs['class'] = 'form-control'
        self.fields['nombre'].widget.attrs['class'] = 'form-control'
        self.fields['pais'].widget.attrs['class'] = 'form-control'