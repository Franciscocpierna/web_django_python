from django.shortcuts import render

# Create your views here.
def index(request):
    print(f"user =  {request.user}")

    if str(request.user) == 'AnonymousUser':
        teste = "usuario não logado"
        
    else:
        teste = "usuario logado"
           
    context = {
        'curso': 'Programação web com Django Framework',
        'outros': 'Django é massa ',
        'logado': teste 

    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')    