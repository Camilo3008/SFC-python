from rest_framework import serializers
from apps.categoria.models import Categoria
from apps.evento.models import Evento
from apps.tipoEvento.models import TipoEvento
from apps.categoria.api.serializers import categoriaCrSerializer
from apps.tipoEvento.api.serializers import TipoEventoSerializer

class EventoSerializer(serializers.ModelSerializer):

    fk_categoria = categoriaCrSerializer()
    fk_tipoEvento = TipoEventoSerializer()
    
    class Meta:
        model = Evento
        fields = ['id', 'nombre', 'fk_categoria', 'fk_tipoEvento', 'cantidadPartes', 'date_start', 'date_end', 'date_modified']



class EventoSerializerCr(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ['id', 'nombre', 'fk_categoria', 'fk_tipoEvento', 'cantidadPartes', 'date_start', 'date_end', 'date_modified']


