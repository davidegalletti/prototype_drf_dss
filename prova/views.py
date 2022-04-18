from django_readers.rest_framework import SpecMixin
from rest_framework.generics import RetrieveAPIView
from prova.models import Regione, Provincia
from prova.serializers import ProvinciaSerializer, Provincia3Serializer
from rest_framework import viewsets

from rest_framework import permissions


class ProvinciaDetail(viewsets.ModelViewSet):
    queryset = Provincia.objects.all()
    serializer_class = ProvinciaSerializer
#    permission_classes = [permissions.IsAuthenticated]


#class Provincia2Detail(viewsets.ModelViewSet):
#    queryset = Provincia.objects.all()
#    serializer_class = Provincia2Serializer
#    permission_classes = [permissions.IsAuthenticated]

class Provincia2DetailView(SpecMixin, RetrieveAPIView):
#    nome = serializers.CharField(max_length=100)
#    regione = RegioneSerializer()
    # queryset = Provincia.objects.all()
    lookup_field = 'id'

    def get_queryset(self):
        self.spec = Provincia.objects.all()
        return self.spec

    def get_spec(self):
        return [
            'id',
            'nome',
            {'regione': [
                'id',
                'nome',
            ]},
        ]

    # spec = [
    #         'id',
    #         'nome',
    #         {'regione': [
    #             'id',
    #             'nome',
    #         ]},
    #     ]


class Provincia3Detail(viewsets.ModelViewSet):
    queryset = Provincia.objects.all()
    serializer_class = Provincia3Serializer
#    permission_classes = [permissions.IsAuthenticated]
