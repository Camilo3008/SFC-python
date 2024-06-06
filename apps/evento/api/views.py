from rest_framework.viewsets import ModelViewSet
from apps.evento.api.serializers import EventoSerializer, EventoSerializerCr
from apps.evento.models import Evento

class EventoViewSet(ModelViewSet):
    serializer_class = EventoSerializer
    queryset = Evento.objects.all()
    http_method_names = ['get', 'delete']

    
class EventoViewSetCr(ModelViewSet):
    serializer_class = EventoSerializerCr
    queryset = Evento.objects.all()
    http_method_names = ['post', 'put']
