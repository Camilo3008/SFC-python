from rest_framework.viewsets import ModelViewSet
from apps.categoria.api.serializers import CategoriaSerializer, categoriaCrSerializer
from apps.categoria.models import Categoria

class CategoriaViewSet(ModelViewSet):
    serializer_class = CategoriaSerializer
    queryset = Categoria.objects.all()
    http_method_names = ['get', 'delete']

class CategoriasCrViewSet(ModelViewSet):
    serializer_class = categoriaCrSerializer
    queryset = Categoria.objects.all()
    http_method_names = ['post', 'put']
