from rest_framework.serializers import ModelSerializer
from Utilidades.models import Utilidade


class UtilidadeSerializer(ModelSerializer):
    class Meta:
        model = Utilidade
        fields = ('nome','descricao','horario_func','idade_minima')
