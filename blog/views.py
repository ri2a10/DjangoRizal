from re import template
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Artikel, Kategori
# Create your views here.

@login_required
def dashboard(request):
    template_name = "back/dashboard.html"
    context = {
        'title':'dashboard',
    }
    return render(request, template_name, context)

@login_required
def artikel(request):
    template_name = "back/tabel_artikel.html"
    artikel = Artikel.objects.all()
    #for a in artikel:
    #    print(a.nama, '-', a.judul, '-',a.kategory)
    context = {
        'title':'tabel artikel',
        'artikel':artikel
    }
    return render(request, template_name, context)

@login_required
def tambah_artikel(request):
    template_name = "back/tambah_artikel.html"
    kategori = Kategori.objects.all()
    print(kategori)
    if request.method == "POST":
        nama = request.POST.get('nama')
        judul = request.POST.get('judul')
        body = request.POST.get('body')
        kategori = request.POST.get('kategori')

        kat = Kategori.objects.get(nama=Kategori)
        Artikel.objects.create(
            nama = nama,
            judul = judul,
            body = body,
            Kategori = kat,
        )
        return redirect(artikel)
    context = {
        'title': 'tambah artikel',
        'kategori':kategori,
    }
    return render(request, template_name, context)

@login_required
def lihat_artikel(request, id):
    template_name = "back/lihat_artikel.html"
    artikel = Artikel.objects.get(id=id)
    context = {
        'title':'lihat artikel',
        'artikel': artikel,
    }
    return render(request, template_name, context)

@login_required
def edit_artikel(request, id):
    template_name = "back/edit_artikel.html"
    a = Artikel.objects.get(id=id)
    if request.method == "POST":
        judul = request.POST.get("judul")
        body = request.POST.get("body")
        print(judul, body)
        a.judul = judul
        a.body = body
        a.save()
        return redirect(artikel)
    context = {
        'title':'edit artikel',
        'artikel':a,
    }
    return render(request, template_name, context)

@login_required
def delete_artikel(request, id):
    Artikel.objects.get(id=id).delete()
    return redirect(artikel)

def users(request):
    tamplate_name = "back/tabel_users.html"
    context = {
        'title':'tabel users'
    }
    return render(request, tamplate_name, context)
        