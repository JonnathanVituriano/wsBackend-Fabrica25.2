from django.shortcuts import render, redirect, get_object_or_404
from .models import Comida, Categoria
from .forms import CategoriaForm, ComidaNomeForm
import requests

from rest_framework import viewsets
from .serializers import ComidaSerializer, CategoriaSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ComidaViewSet(viewsets.ModelViewSet):
    queryset = Comida.objects.all()
    serializer_class = ComidaSerializer

def adicionar_categoria(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listar_comidas")
    else:
        form = CategoriaForm()
    return render(request, "adicionarCategoria.html", {"form": form})

def listar_comidas(request):
    comidas = Comida.objects.all()
    return render(request, "listarComidas.html", {"comidas": comidas})

def adicionar_comida(request):
    if request.method == "POST":
        form = ComidaNomeForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data["nome"]
            
            url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={nome}"
            resposta = requests.get(url)
            data = resposta.json()
            meals = data.get("meals")
            if meals:
                meal = meals[0]
                
                categoria_nome = meal.get("strCategory", "Sem Categoria")
                categoria, _ = Categoria.objects.get_or_create(nome=categoria_nome)
                comida = Comida(
                    id=meal["idMeal"],
                    nome=meal["strMeal"],
                    categoria=categoria,
                    area=meal.get("strArea", ""),
                    instrucoes=meal.get("strInstructions", ""),
                    imagem=meal.get("strMealThumb", "")
                )
                comida.save()
                return redirect("listar_comidas")
            else:
                form.add_error("nome", "Comida não encontrada na API.")
    else:
        form = ComidaNomeForm()
    return render(request, "adicionarComida.html", {"form": form})
    
def editar_comida(request, pk):
    comida = get_object_or_404(Comida, pk=pk)
    from .forms import ComidaNomeForm
    if request.method == "POST":
        form = ComidaNomeForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data["nome"]
            url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={nome}"
            resposta = requests.get(url)
            data = resposta.json()
            meals = data.get("meals")
            if meals:
                meal = meals[0]
                categoria_nome = meal.get("strCategory", "Sem Categoria")
                categoria, _ = Categoria.objects.get_or_create(nome=categoria_nome)
                comida.nome = meal["strMeal"]
                comida.categoria = categoria
                comida.area = meal.get("strArea", "")
                comida.instrucoes = meal.get("strInstructions", "")
                comida.imagem = meal.get("strMealThumb", "")
                comida.save()
                return redirect("listar_comidas")
            else:
                form.add_error("nome", "Comida não encontrada na API.")
    else:
        form = ComidaNomeForm(initial={"nome": comida.nome})
    return render(request, "editarComida.html", {"form": form, "comida": comida})

def deletar_comida(request, pk):
    comida = get_object_or_404(Comida, pk=pk)
    if request.method == "POST":
        comida.delete()
        return redirect("listar_comidas")
    return render(request, "deletarComida.html", {"comida": comida})

def buscar_comidas_api(request):
    termo = request.GET.get("termo","")
    comidas_api = []
    if termo:
        url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={termo}"
        resposta = requests.get(url)
        data = resposta.json()
        comidas_api = data.get("meals", [])
    return render(request, "buscarComidasApi.html", {"comidas_api": comidas_api, "termo": termo})