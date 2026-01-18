from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContatoForm, ProdutoModelForm
from .models import Produto

def index(request):
    context = {
        'produtos': Produto.objects.all()
    }
    return render(request, 'index.html', context)

def contato(request):
    form = ContatoForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.send_mail()
            messages.success(request, 'E-mail enviado com sucesso!')
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar e-mail')
    
    context = {
        'form': form
    }
    return render(request, 'contato.html', context)

def produto(request):
    # Verificação mais robusta do que comparar String
    if request.user.is_authenticated:       # if str(request.user) != 'AnonymousUser':
        if request.method == 'POST':
            form = ProdutoModelForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'Produto salvo com sucesso.')
                form = ProdutoModelForm()
            else:
                messages.error(request, 'Erro ao salvar produto.')
        else:
            form = ProdutoModelForm()
        
        context = {
            'form': form
        }
        return render(request, 'produto.html', context)
    else:
        # Se o erro persistir aqui, verifique se 'index' está definido em urls.py
        return redirect('index')


   
