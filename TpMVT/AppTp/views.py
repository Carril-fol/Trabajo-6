from django.shortcuts import render
from django.http import HttpResponse
from AppTp.models import Familia

# Create your views here.
def lista_familia(request):
    context = {
        'familiares': Familia.objects.all()
    }
    return render(request, r'C:\Users\folco\Desktop\Tp\TpMVT\AppTp\plantillas\index.html',context)