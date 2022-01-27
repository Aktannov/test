from django.shortcuts import render, redirect

from main.forms import TaskForm
from main.models import Task


def index(request):
    task = Task.objects.order_by('id')
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': task})


def about(request):
    return render(request, 'main/about.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Error'

    form = TaskForm()
    context = {
        'form': form
    }
    return render(request, 'main/create.html', context)


