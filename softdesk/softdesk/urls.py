from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api.views.project import ProjectViewSet
from api.views.issue import IssueViewSet
from api.views.comment import CommentViewSet
from api.views.contributor import ContributorViewSet
from api.views.signup import SignupView
from front.urls import front_urlpatterns


router = routers.SimpleRouter()
router.register('projects', ProjectViewSet, basename='project')
router.register(r'projects/(?P<id>\d+)/issues', IssueViewSet, basename='issue')
router.register('issues', IssueViewSet, basename='issue')
router.register('comment', CommentViewSet, basename='comment')
router.register('contributor', ContributorViewSet, basename='contributor')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
    path('api/signup/', SignupView.as_view(), name='signup'),
    path(r'api/projects/<int:id>/issues', IssueViewSet.as_view({'get': 'get_project_issues'}), name="project_issues"),
    path('front/', include(front_urlpatterns)),
]
