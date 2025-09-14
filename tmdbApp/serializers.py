from rest_framework import serializers
from .models import Comida, Categoria

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nome']

class ComidaSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer(read_only=True)
    categoria_id = serializers.PrimaryKeyRelatedField(
        queryset=Categoria.objects.all(), source='categoria', write_only=True
    )
    class Meta:
        model = Comida
        fields = ['id', 'nome', 'categoria', 'categoria_id', 'area', 'instrucoes', 'imagem']
