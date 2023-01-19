from django.urls import path
from front.views import project_list, project_detail


front_urlpatterns = [
    path('', project_list, name='project-list'),
    path('projectdetail/<int:project_id>', project_detail, name='projectdetail'),
]
