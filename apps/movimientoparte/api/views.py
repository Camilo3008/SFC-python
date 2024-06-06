from rest_framework.viewsets import ModelViewSet
from apps.movimientoparte.api.serializers import MovimientoParteSerializer
from apps.movimientoparte.models import MovimientoParte

from apps.movimientoparte.api.serializers import MovimientoParteSerializerRegist


class MovimientoParteViewSet(ModelViewSet):
    serializer_class = MovimientoParteSerializer
    queryset = MovimientoParte.objects.all()
    http_method_names = ['get', 'delete']


class MovimientoParteViewSetRegist(ModelViewSet):
    serializer_class = MovimientoParteSerializerRegist
    queryset = MovimientoParte.objects.all()
    http_method_names = ['post', 'put']
