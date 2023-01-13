from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.views import ProjectViewSet


router = routers.SimpleRouter()
router.register('project', ProjectViewSet, basename='project')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls)),
]
