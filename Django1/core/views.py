from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Produto
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    print(f"user =  {request.user}")

    produtos = Produto.objects.all()
           
    context = {
        'curso': 'Programação web com Django Framework',
        'outros': 'Django é massa ',
        'produtos': produtos

    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')    

def produto(request, id):
    #prod = Produto.objects.get(id=id)
    prod = get_object_or_404(Produto, id=id)
    context={
        'produto': prod
    }
    return render(request, 'produto.html',context)    
    #return render(request, 'produto.html', {'produto': produto})    

def error404(request, ex):
   template = loader.get_template('404.html')  
   return HttpResponse(content=template.render(), content_type = 'text/html; charset= utf8', status=404)
def error500(request):
    template = loader.get_template('500.html')  
    return HttpResponse(content=template.render(), content_type = 'text/html; charset= utf8', status=500)