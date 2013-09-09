from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from Solvent.social.models import User, Project, Attachment

def index(request):
    recent_users = User.objects.all().order_by('-last_active')[:5]
    recent_projects = Project.objects.all().order_by('-last_activity')[:5]
    context = { 'recent_users': recent_users, 'recent_projects': recent_projects }
    return render(request, 'index.html', context)

def users(request):
    all_users = User.objects.all()
    context = { 'all_users': all_users }
    return render(request, 'users/users.html', context)

def userDetail(request, user_id):
    user = User.objects.get(pk=user_id)
    context = { 'user': user }
    return render(request, 'users/detail.html', context)

def projects(request):
    all_projects = Project.objects.all()
    context = { 'all_projects': all_projects }
    return render(request, 'projects/projects.html', context)

def projectDetail(request, project_id):
    project = Project.objects.get(pk=project_id)
    context = { 'project': project }
    return render(request, 'projects/detail.html', context)

def attachmentDetail(request, attachment_id):
    attachment = Attachment.objects.get(pk=attachment_id)
    context = { 'attachment': attachment }
    return render(request, 'attachments/detail.html', context)



