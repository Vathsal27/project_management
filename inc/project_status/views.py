import re
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Project

# Create your views here.
def home(request):
    data = Project.objects.all()
    dict = {
        'data':data,
    }
    return render(request, 'project_status/index.html', dict)
    

def project_details(request, project_id):
    project = Project.objects.get(pk=project_id)
    if request.method == 'POST':
        if (request.POST.get("project_visit_add")):
            project.visits += 1
        if (request.POST.get("project_visit_sub")):
            project.visits -= 1

        is_checked = request.POST.get('status') == 'on'
        if is_checked:
            project.status = True
        else:
            project.status = False

        project.save()
        return redirect("home")
    return render(request, 'project_status/project_details.html', {'project':project})
