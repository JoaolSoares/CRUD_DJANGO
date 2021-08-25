from django.shortcuts import render, redirect, resolve_url
from .models import Pessoas
from .form import pessoasform

# Create your views here.
# view da home (READ).
def home(request):
    data = {}  # Cria um dict para ser usado no front
    data['pessoas'] = Pessoas.objects.all()  # Puxa os dados do db
    return render(request, 'home/home.html', data)  # Envia as informações para o front

# view do formulario (CREATE).
# tambem será usado para o UPDATE e DELETE.
def formulario(request):
    data = {}
    form = pessoasform(request.POST or None)  # Pergunta se o formulario ja tem ou não resposta.

    if form.is_valid():
        form.save()
        return redirect('url_home')  # Volta para a home

    data['form'] = form
    return render(request, 'home/form.html', data)


def update(request, pk):
    data = {}
    pessoa = Pessoas.objects.get(pk=pk)  # Da um get na primary key.
    form = pessoasform(request.POST or None, instance=pessoa)  # instance é para as infos continuarem
                                                               # no update
    if form.is_valid():
        form.save()
        return redirect('url_home')

    data['form'] = form
    data['pessoa'] = pessoa  # Envia os dados do pessoa pro form.html para ser usado no DELETE.
    return render(request, 'home/form.html', data)


def delete(request, pk):
    pessoa = Pessoas.objects.get(pk=pk)
    pessoa.delete()
    return redirect('url_home')
