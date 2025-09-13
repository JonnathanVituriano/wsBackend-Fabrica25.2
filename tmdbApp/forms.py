from django import forms
from .models import Comida, Categoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ["nome"]

class ComidaForm(forms.ModelForm):
    class Meta:
        model = Comida
        fields = ["id", "nome", "categoria", "area", "instrucoes", "imagem"]