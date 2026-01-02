from django.shortcuts import render
from .models import Produto

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
    prod = Produto.objects.get(id=id)
    context={
        'produto': prod
    }
    return render(request, 'produto.html',context)    
    #return render(request, 'produto.html', {'produto': produto})    