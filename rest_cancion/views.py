from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from youmusic.models import Cancion
from rest_cancion.serializers import CancionSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated




@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def lista_cancion(request):

    if request.method == 'GET':
        listaCancion =  Cancion.objects.all()
        serializer = CancionSerializer(listaCancion, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        dataP = JSONParser().parse(request)
        serializer = CancionSerializer(data = dataP)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def detalle_cancion(request, id):
    try:
        cancion = Cancion.objects.get(idCancion=id)
    except Cancion.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        seriaz =  CancionSerializer(cancion)
        return Response(seriaz.data)
    elif request.method == "PUT":
        dataP = JSONParser().parse(request)
        seriaz =  CancionSerializer(cancion, data=dataP)
        if seriaz.is_valid():
            seriaz.save()
            return Response(seriaz.data)
        else:
            return Response(seriaz.errors, status = status.HTTP_400_BAD_REQUEST)            
    elif request.method == "DELETE":
        cancion.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
