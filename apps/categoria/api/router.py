from rest_framework.routers import DefaultRouter

from apps.categoria.api.views import CategoriaViewSet, CategoriasCrViewSet

router_categoria = DefaultRouter()
router_categoria.register(prefix='categoria', basename='categoria', viewset=CategoriaViewSet)
router_categoria.register(prefix='categoriaRegister', basename='categoriaRegister', viewset=CategoriasCrViewSet)