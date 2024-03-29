from django.contrib import admin
from django.db import router
from django.urls import path, include


from rest_framework.routers import DefaultRouter

from core.views import CategoriaViewSet, EditoraViewSet

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'editoras', EditoraViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
    ]