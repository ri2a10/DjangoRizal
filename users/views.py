from django.shortcuts import render

def list_users(request):
    template_name = "users.html"
    context = {
        'title':'list users',
    }
    return render(request, template_name,context)

# Create your views here.
