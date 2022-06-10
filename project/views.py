from django.shortcuts import redirect, render
from . models import Project
from . forms import ProjectCreationForm

def projects(request):
    projects = Project.objects.all()
    context = {'projects':projects}
    return render(request, 'project/projects.html', context)

def singleProject(request, pk):
    project = Project.objects.get(id=pk)
    context = {'project':project}
    return render(request, 'project/single-project.html', context)

def createProject(request):
    form = ProjectCreationForm()
    if request.method == "POST":
        form = ProjectCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("projects")
    context= {'form':form}
    return render(request, 'form-template.html', context)


def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectCreationForm(instance=project)
    if request.method == "POST":
        form = ProjectCreationForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect("projects")    
    context = {'form':form, 'project':project}
    return render(request, 'form-template.html', context)

def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == "POST":
        project.delete()
        return redirect("projects")

    context = {}
    return render(request, 'project/delete.html', context)