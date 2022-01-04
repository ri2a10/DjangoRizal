from django.shortcuts import render, redirect
from django.contrib.auth import authenticate 
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout

from blog.models import Artikel
from users.models import Biodata


def index(request):
    template_name = 'front/index.html'
    artikel = Artikel.objects.all()
    context = {
        'title':'halaman awal',
        'artikel':artikel
        }
    return render(request, template_name, context)

def about(request):
    template_name = 'front/about.html'
    context = {
        'title':'about me'
    }

    return render(request, template_name, context)

def login(request):
    if request.user.is_authenticated:
    
        return redirect('index')
    template_mane ="account/login.html"
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print('username benar')
            auth_login(request, user)
            return redirect('index')
        else:
            print('username salah')

    context = {
        'title':'from login'
    }
    return render(request, template_mane,context)

def logout_view(request):
    logout(request)
    return redirect('index')

def registerasi(request):
    template_name = "account/register.html"
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        nama_depan = request.POST.get('nama_depan')
        nama_belakang = request.POST.get('nama_belakang')
        alamat = request.POST.get('alamat')
        no_telepon = request.POST.get('no_telepon')
        
        User.objects.create(
            username = username,
            password = password,
            first_name = nama_depan,
            last_name = nama_belakang,
            email = email
        )
        Biodata.objects.create(
            user = User,
            alamat = alamat,
            no_telepon = no_telepon

        )
        return redirect(index)
        

        
    context = {
        'title':'form registrasi'
    }
    return render(request, template_name, context)
    
      

