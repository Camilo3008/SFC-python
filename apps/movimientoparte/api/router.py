from rest_framework.routers import DefaultRouter

from apps.movimientoparte.api.views import MovimientoParteViewSet

from apps.movimientoparte.api.views import MovimientoParteViewSetRegist

router_movimientoParte = DefaultRouter()
router_movimientoParte.register(prefix="movimientoParte", basename="MovimientoParte", viewset=MovimientoParteViewSet)

router_movimientoParte.register(prefix="movimientoParteRegist", basename="MovimientoParteRegist", viewset=MovimientoParteViewSetRegist)

