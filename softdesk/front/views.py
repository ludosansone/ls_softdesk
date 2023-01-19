from django.shortcuts import render
import requests


def project_list(request):
    uri = 'http://localhost:8000/api/project'
    response = requests.get(uri).json()

    return render(request, 'front/project-list.html', {'response': response, 'uri': uri})


def project_detail(request, project_id):
    uri = f'http://localhost:8000/api/project/{project_id}'
    project = requests.get(uri).json()

    return render(request, 'front/project-detail.html', {'project': project, 'uri': uri})
