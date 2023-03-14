from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api.views.project import ProjectViewSet
from api.views.issue import IssueViewSet
from api.views.comment import CommentViewSet
from api.views.contributor import ContributorViewSet
from api.views.signup import SignupView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from rest_framework import permissions


router = routers.SimpleRouter()
router.register('projects', ProjectViewSet, basename='project')
router.register(r'projects/(?P<id>\d+)/users', ContributorViewSet, basename='contributor')
router.register(r'projects/(?P<id>\d+)/issues/(?P<issue_id>\d+)/comments', CommentViewSet, basename='comment')
router.register(r'projects/(?P<id>\d+)/issues', IssueViewSet, basename='projects_issues')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
    path('api/signup/', SignupView.as_view(), name='signup'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
