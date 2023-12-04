from rest_framework import serializers
from app.models import Users

class UsersSerializer(serializers.ModelSerializer):
   
    class Meta:
        #Hacemos correspondencia del serializador con la el modelo
        model = Users
        fields = ['id','nombre','apellido','email','edad','pais','ciudad','domicilio','codigoPostal','contrasena','avatar']