import requests
import hashlib
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Produk, Kategori, Status
from .forms import ProdukForm

# Create your views here.
def import_produk(request):
    url = 'https://recruitment.fastprint.co.id/tes/api_tes_programmer'

    now = datetime.now()
    username=f"tesprogrammer{now.strftime('%d%m%y')}C{now.strftime('%H')}"
    password_plain=f"bisacoding-{now.strftime('%d-%m-%y')}"

    password_md5 = hashlib.md5(password_plain.encode()).hexdigest()

    payload={
        "username": username,
        "password": password_md5
    }

    response = requests.post(url, data=payload)

    if response.status_code != 200:
        return HttpResponse('Import Produk Gagal')
    

    data = response.json().get('data')

    for item in data:
        kategori, _ = Kategori.objects.get_or_create(
            nama_kategori=item["kategori"]
        )

        status, _ = Status.objects.get_or_create(
            nama_status=item["status"]
        )

        Produk.objects.update_or_create(
            id_produk=item["id_produk"],
            defaults={
                "nama_produk": item["nama_produk"],
                "harga": int(item["harga"]),
                "kategori": kategori,
                "status": status
            }
        )

    
    return HttpResponse(f"Import Berhasil ({len(data)}) produk)")

def produk_list(request):
    produk=Produk.objects.all()
    return render(request, 'produk/list.html', {'produk':produk})

def produk_tambah(request):
    form = ProdukForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('produk_list')
    
    return render(request, 'produk/form.html', {'form':form, 'title':'Tambah Produk'})

def produk_edit(request, id):
    produk = get_object_or_404(Produk, id_produk=id)
    
    form = ProdukForm(request.POST or None, instance=produk)
    if form.is_valid():
        form.save()
        return redirect('produk_list')
    
    return render(request, 'produk/form.html', {'form':form, 'title': 'Edit Produk'})

def produk_hapus(request, id):
    produk = get_object_or_404(Produk, id_produk=id)
    produk.delete()
    return redirect('produk_list')