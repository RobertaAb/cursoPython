from django.shortcuts import render

# Create your views here.


def index(request):
    nome = "teste "
    return render(request, 'estoque/base.html', {'nome': nome})