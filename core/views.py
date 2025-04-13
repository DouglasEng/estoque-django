from django.shortcuts import render, get_object_or_404
from .models import Produto
from django.http import HttpResponse
from django.template import loader

def index(request):
    produtos = Produto.objects.all()
    context = {
        'curso': 'Programando com Django',
        'produtos': produtos
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')

def produto(request, pk):
    # produtos = Produto.objects.get(id=pk)
    produtos = get_object_or_404(Produto, id=pk)
    context = {
        'produto': produtos
    }
    return render(request, 'produto.html', context)

def error404(request, exception=None):  
    template = loader.get_template('error404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf-8', status=404)

def error500(request, exception=None):  
    template = loader.get_template('error500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf-8', status=500)

