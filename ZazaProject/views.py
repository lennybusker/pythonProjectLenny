from django.shortcuts import render


def index(request):
    return render(request, 'ZazaProject/ZazaHTML.html')
# Create your views here.
