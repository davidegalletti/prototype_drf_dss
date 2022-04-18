from rest_framework import routers, serializers
from prova.models import Provincia, Regione
from rest_framework.generics import RetrieveAPIView


class RegioneSerializer(serializers.Serializer):
    nome = serializers.CharField(max_length=100)


class ProvinciaSerializer(serializers.Serializer):
    nome = serializers.CharField(max_length=100)
    regione = RegioneSerializer()


class Provincia3Serializer(serializers.Serializer):
    id = serializers.IntegerField()
    nome = serializers.CharField(max_length=100)
    regione = RegioneSerializer()


