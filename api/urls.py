from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView
from api.views import CategoriaViewSet, ClienteCriarView, CustomTokenObtainPairView, JogoViewSet, JogoPorCategoriaView


router = routers.DefaultRouter()
router.register('categorias', CategoriaViewSet)
router.register('jogos', JogoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('cliente/cadastro/', ClienteCriarView.as_view(), name='registro_cliente'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('jogos-por-categoria', JogoPorCategoriaView.as_view(), name='jogos_por_categoria')
]