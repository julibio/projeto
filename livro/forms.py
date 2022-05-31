from django import forms
from .models import Item
class ItemForm(forms.ModelForm):
   class Meta:
       model = Item
       fields = [ 'item_nome', 'item_desc', 'item_preco', 'item_imagem']
