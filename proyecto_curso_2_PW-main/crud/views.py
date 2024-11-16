from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


from .models import BleachCharacter
# Create your views here.
def index(request):
    list_bleachCharacter = BleachCharacter.objects.all()
    template = loader.get_template("index.html")
    context = {"Bleach_Characters":list_bleachCharacter}
    return HttpResponse(template.render(context,request))

def vista_detalle(request, id_bleachCharacter):
    character_detail = BleachCharacter.objects.get(id = id_bleachCharacter)
    template = loader.get_template("detail.html")
    context = {"bleachCharacter":character_detail}
    return HttpResponse(template.render(context,request))