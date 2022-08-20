from posixpath import split
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from django.db.models import Q
from .models import Movies, Director, Actors,Genero, Series



# Create your views here.
def contenido(request):
    return render(request, "contenido.html")

def movies(request):
    q_filtro = request.GET.get('q_filtro') if request.GET.get('q_filtro') != None else ''
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    comp = Genero.objects.all()
    movs = Movies.objects.filter(Q(generof__name__icontains = q_filtro), Q(name__icontains = q))
    context = {
        'movs': movs,
        'comp': comp,
    }
    return render(request, 'src/movies.html', context)


def series(request):
    q_filtro = request.GET.get('q_filtro') if request.GET.get('q_filtro') != None else ''
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    comp = Genero.objects.all()
    sers = Series.objects.filter(Q(generof__name__icontains = q_filtro), Q(name__icontains = q))
    context = {
        'sers': sers,
        'comp': comp,
    }
    return render(request, 'src/series.html', context)


def descriptionInfo(request, pk):
    # Tenemos que quitar residuos
    q_movie = request.GET.get('q_movie') if request.GET.get('q_movie') != None else ''
    movsQ = Movies.objects.filter(id = pk)
    context = {
        'movsQ': movsQ,
    }
    return render(request,'description.html', context)

def descriptionInfoSeries(request, pk):
    # Tenemos que quitar residuos
    q_movie = request.GET.get('q_movie') if request.GET.get('q_movie') != None else ''
    movsQ = Series.objects.filter(id = pk)
    context = {
        'movsQ': movsQ,
    }
    return render(request,'description.html', context)

def browser(request):
    # Aqui recibimos todas las queries
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    brows = Movies.objects.filter(name__icontains = q)
    browstwo = Series.objects.filter(name__icontains = q)
    context = {
        'brows':brows,
        'browstwo':browstwo,
    }
    return render(request, 'browser.html', context)

def codigoqr(request):
    return render(request, 'codigoqr.html')