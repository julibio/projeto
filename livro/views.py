from django.shortcuts import render,redirect
from django.http import HttpResponse
from livro.models import Item
from django.template import loader
from django import forms
from .forms import ItemForm
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
import pandas as pd


# Create your views here.



def index(request):
    #return HttpResponse('Página Inicial da Lista de Livros')
    return render(request, 'livro/index.html')

class ListaC(ListView):
    model = Item
    context_object_name = 'item_lista'
    template_name = 'livro/lista.html'
    paginate_by = 3
    #http://127.0.0.1:8000/loja/lista/?page=1

def lista(request):
      try:
        item_lista=Item.objects.all()
        template = loader.get_template('livro/lista.html')
        context={'item_lista':item_lista,
        }
        return HttpResponse(template.render(context,request))
      except:
         return HttpResponse('<h1>Erro ao Listar Objetos!</h1>')

@login_required
def detail(request,item_id):
   item = Item.objects.get(pk=item_id)
   context = { 'item':item, }
   return render(request,'livro/detail.html',context)
   
@login_required(login_url='livro:lista')
def cadastro(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
          form.save()
          return redirect('livro:lista')
    return render(request, 'livro/form.html', {'form':form})

def editar(request,id):
    item=Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
      form.save()
      return redirect('livro:lista')
    return render(request, 'livro/form.html', {'form':form,'item':item})

def deletar(request,id):
    item=Item.objects.get(id=id)
    if request.method == 'POST':
      item.delete()
      return redirect('livro:index')
    return render(request, 'livro/item_deletado.html', {'item':item}) 

def relatorio(request):
    item = Item.objects.all().values()
    df = pd.DataFrame(item)
    mydict = {
       'df': df.to_html()
    }
    return render(request, 'livro/relatorio.html', context=mydict)

def html(request):
    return render(request, 'livro/html.html')
