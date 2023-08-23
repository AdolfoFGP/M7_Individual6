from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import TaskForm, TaskFilterForm

def login_view(request):
    error_message = None
    if request.method == 'POST':
        # Procesar el formulario de inicio de sesión
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('task_manager_app:welcome')
        else:
            # Mostrar un mensaje de error en la plantilla
            error_message = "Credenciales incorrectas."
    
    return render(request, 'task_manager_app/login.html', {'error_message': error_message})

def logout_view(request):
    logout(request)
    return redirect('task_manager_app:welcome')

def welcome_view(request):
    return render(request, 'task_manager_app/welcome.html')

def task_list_view(request):
    tasks = Task.objects.filter(user=request.user).order_by('due_date')

    form = TaskFilterForm(request.GET)
    if form.is_valid():
        state = form.cleaned_data['state']
        label = form.cleaned_data['label']

        if state:
            tasks = tasks.filter(state=state)
        if label:
            tasks = tasks.filter(label=label)

    # Si se envió el formulario o se hizo clic en "Clear Filter", mostrar todas las tareas
    if request.method == 'GET' and not form.is_bound:
        tasks = Task.objects.filter(user=request.user).order_by('due_date')

    return render(request, 'task_manager_app/task_list.html', {'tasks': tasks, 'form': form})



'''def task_detail_view(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'task_manager_app/task_detail.html', {'task': task})'''

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_manager_app:login')  # Redirigir al login después de registro exitoso
    else:
        form = UserCreationForm()
    return render(request, 'task_manager_app/register.html', {'form': form})




def task_create_view(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_manager_app:task_list')  # Redirige al listado de tareas
    else:
        form = TaskForm()
    return render(request, 'task_manager_app/task_create.html', {'form': form})

def task_delete_view(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('task_manager_app:task_list')  # Redirige al listado de tareas
    return render(request, 'task_manager_app/task_delete.html', {'task': task})


def task_detail_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    
    if request.method == 'POST':
        observations = request.POST.get('observations', '')
        task.observations = observations
        task.save()
        return redirect('task_manager_app:task_detail', pk=pk)

    context = {'task': task}
    return render(request, 'task_manager_app/task_detail.html', context)

def task_edit_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_manager_app:task_list')  # Redirige al listado de tareas
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_manager_app/task_edit.html', {'form': form, 'task': task})

def task_complete_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.state = 'completada'
    task.save()
    return redirect('task_manager_app:task_list')  # Redirige al listado de tareas
