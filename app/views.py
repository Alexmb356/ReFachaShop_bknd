from django.shortcuts import render
from django.http import HttpResponse

from app.models import Users

from app import serializers

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
def index(request) :
    return HttpResponse ('<h1>Hola Mundo Django</h1>')
    
@api_view(['GET']) 
def get_users(request):
    """
    Lista todos los usuarios
    """
    #se buscan todos los registros guardados en la base
    users = Users.objects.all() #SELECT * FROM app_movie
    #cuando estás serializando múltiples instancias de un modelo
    serializer = serializers.UsersSerializer(users, many=True)
    #Response es una clase que me permite devolver una respuesta
    #que cumple con los estandares de API-REST
    return Response(serializer.data)

@api_view(['POST'])
def create_user(request):
    #Se seriala los datos recibidos desde el formulario
    serializer = serializers.UsersSerializer(data=request.data)
    #Se ejecutan las validaciones
    if serializer.is_valid():
        #Se registra en base de datos
        serializer.save()
        #Se genera la respuesta que deseamos devolver
        response = {'status':'Ok',
                    'message':'Usuario creado exitosamente',
                    'data':serializer.data}
        return Response(data= response, status=status.HTTP_201_CREATED)
    
    response = {'status':'Error',
                'message':'No se pudo crear el usuario',
                'errors':serializer.errors}
    return Response(data=response, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_user(request, id):
    """
    Eliminar una pelicula.
    """
    try:
        user = Users.objects.get(pk=id)        
    except Users.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,data='Recurso no encontrado')
    #Se elimina la pelicula en base de datos
    user.delete()
    return Response({'message':'Se elimino el usuario'},status=status.HTTP_200_OK)

@api_view(['PUT'])
def update_user(request, id):
    """
    Actualiza una pelicula.
    """
    try:
        user = Users.objects.get(pk=id)
    except Users.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,data='Recurso no encontrado')
    
    serializer = serializers.UsersSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        response = {'status':'Ok',
                    'message':'Pelicula modificada exitosamente',
                    'data':serializer.data}
        return Response(data=response)
    response = {'status':'Error',
                'message':'No se pudo modificar la pelicula',
                'errors':serializer.errors}
    return Response(data=response, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def detail_user(request, id):
    """
    Muestra una pelicula.
    """
    try:
        #Se busca la pelicula en base por el id
        user = Users.objects.get(pk=id)        
    except Users.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,data='Recurso no encontrado')

    serializer = serializers.UsersSerializer(user)
    return Response(serializer.data)
