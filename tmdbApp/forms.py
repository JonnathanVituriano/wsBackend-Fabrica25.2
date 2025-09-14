from django import forms
from .models import Comida, Categoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ["nome"]


class ComidaNomeForm(forms.Form):
    nome = forms.CharField(label="Nome da comida", max_length=200)