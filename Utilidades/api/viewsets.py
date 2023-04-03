from rest_framework.viewsets import ModelViewSet
from Utilidades.models import Utilidade
from .serializers import UtilidadeSerializer


class UtilidadesViewSet(ModelViewSet):

    queryset = Utilidade.objects.all()
    serializer_class = UtilidadeSerializer
