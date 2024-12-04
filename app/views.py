from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.admin.views.decorators import staff_member_required
from .models import Resource 
from collections import Counter
from .forms import ResourceForm
import json
# Create your views here.
#Página inicial
def home(request):
    return render(request, 'home.html')

#Formulário de cadastro de Usuário
def create(request):
    return render(request, 'create.html')

#INserção dos dados dos usuários no banco
def store(request):
    data = {}
    if(request.POST['password'] != request.POST['password-conf']):
        data['msg'] = 'Senha e confirmação de senha diferentes!'
        data['class'] = 'alert-danger'
    else:
        user = User.objects.create_user(request.POST['name'], request.POST['email'], request.POST['password'])
        user.first_name = request.POST['name']
        user.save()
        user.user_permissions.add(25)
        data['msg'] = 'Usuário cadastrado com sucesso!'
        data['class'] = 'alert-success'
    return render(request, 'create.html', data)

#Formulário do painel de login
def painel(request):
    return render(request, 'painel.html')

#Processa o login
def dologin(request):
    data = {}
    user = authenticate(username=request.POST['user'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect('/dashboard/')
    else:
        data['msg'] = 'Usuário ou senha incorretos!'
        data['class'] = 'alert-danger'
        return render(request, 'painel.html', data)

#Página inicial do dashboard
def dashboard(request): 
    resources = Resource.objects.all() 
    total_resources = resources.count() 
    resource_types = [resource.type for resource in resources] 

    # Contando os tipos de recursos 
    resource_type_counts = Counter(resource_types)
    
    data = { 
        'total_resources': total_resources, 
        'resource_type_labels': list(resource_type_counts.keys()),
        'resource_type_data': list(resource_type_counts.values()),
        'resources': resources,
        'is_admin': request.user.is_staff, 
        }

    data['resource_type_labels_json'] = json.dumps(data['resource_type_labels'])
    data['resource_type_data_json'] = json.dumps(data['resource_type_data'])

    return render(request, 'dashboard/home.html', data)

#Logout do sistema
def logouts(request):
    logout(request)
    return redirect('/painel/')

#Alterar a senha
def changePassword(request):
    user = User.objects.get(email=request.user.email)
    user.set_password('123456')
    user.save()
    logout(request)
    return redirect('/painel/')

# Gestão de Recursos 
def add_resource(request): 
    if request.method == 'POST': 
        form = ResourceForm(request.POST) 
        if form.is_valid(): 
            form.save() 
            return redirect('dashboard') 
    else: 
        form = ResourceForm() 
    return render(request, 'dashboard/add_resource.html', {'form': form}) 

@staff_member_required
def edit_resource(request, id): 
    resource = get_object_or_404(Resource, id=id) 
    if request.method == 'POST': 
        form = ResourceForm(request.POST, instance=resource) 
        if form.is_valid(): 
            form.save() 
            return redirect('dashboard') 
    else: 
        form = ResourceForm(instance=resource) 
        return render(request, 'dashboard/edit_resource.html', {'form': form})

@staff_member_required
def delete_resource(request, id): 
    resource = get_object_or_404(Resource, id=id) 
    resource.delete() 
    return redirect('dashboard')