from rest_framework.viewsets import ModelViewSet
from apps.municipio.api.serializers import MunicipioSerializer, MunicipioSerializerCr
from apps.municipio.models import Municipio

class MunicipioViewSet(ModelViewSet):
    serializer_class = MunicipioSerializer
    queryset = Municipio.objects.all()
    http_method_names = ['get', 'delete']

class MunicipioViewSetCr(ModelViewSet):
    serializer_class = MunicipioSerializerCr
    queryset = Municipio.objects.all()
    http_method_names = ['post', 'put']