from django.db import models

# Create your models here.
class Item(models.Model):
    item_nome=models.CharField(max_length=200)
    item_desc=models.CharField(max_length=200)
    item_preco=models.FloatField()
    item_email=models.EmailField(max_length = 60,null=True)
    item_imagem = models.CharField(max_length=800, default='https://cdn-icons-png.flaticon.com/512/459/459122.png')
 

    def __str__(self):
        return self.item_nome
