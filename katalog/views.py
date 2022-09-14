from django.shortcuts import render
from katalog.models import CatalogItem

def show_katalog(request):
    data_barang_katalog = CatalogItem.objects.all()
    context = {
        'list_katalog': data_barang_katalog,
        'nama': 'Ikra Bhaktiananda',
        'npm' : '2106637580'
    }
    return render(request, "katalog.html", context)