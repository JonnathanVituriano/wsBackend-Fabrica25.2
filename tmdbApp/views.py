from django.shortcuts import render, redirect, get_object_or_404
from .models import Comida
from .forms import ComidaForm
import requests

# Create your views here.

def listar_comidas(request):
    comidas = Comida.objects.all()
    return render(request, "listarComidas.html", {"comidas": comidas})

def adicionar_comida(request):
    if request.method == "POST":
        form = ComidaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listar_comidas")
    else:
        form = ComidaForm()
    return render(request, "adicionarComida.html", {"form": form})
    
def editar_comida(request, pk):
    comida = get_object_or_404(Comida, pk=pk)
    if request.method == "POST":
        form = ComidaForm(request.POST, instance=comida)
        if form.is_valid():
            form.save()
            return redirect("listar_comidas")
    else:
        form = ComidaForm(instance=comida)
    return render(request, "editarComida.html", {"form": form})

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