from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request) :
    return HttpResponse ('<h1>Hola Mundo Django</h1>')
    
def get_users(request) :
    return HttpResponse ('<h2>Listado de Usuarios</h2>') 

def delete_user(request) :
    return HttpResponse ('<h2>Usuario Eliminado</h2>') 