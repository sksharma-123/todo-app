from django.shortcuts import redirect, render
from .models import Task
from django.db import IntegrityError
from django.contrib import messages


def index(request):
    if request.method == "POST":
        task = request.POST['task']

        if task == "":
            messages.add_message(request, messages.WARNING, 'Please add some activity to your routine')
            return redirect('/')

        try:
            x = Task.objects.create(task=task)
            x.save()
        except IntegrityError:
            messages.add_message(request, messages.ERROR, 'This activity already exists in your routine')
            return redirect('/')


    tasks = Task.objects.all()
    just_added_tasks = Task.objects.filter(status="Just Added")
    pending_tasks = Task.objects.filter(status="Pending")
    completed_tasks = Task.objects.filter(status="Completed")

    all_tasks = []
    for task in tasks:
        all_tasks.append(task.task)

    context = {
        'tasks': tasks,
        'all_tasks': all_tasks,
        'just_added_tasks': just_added_tasks,
        'pending_tasks': pending_tasks,
        'completed_tasks': completed_tasks,
    }
    return render(request, 'index.html', context)



def deleteTask(request, id):
    Task.objects.get(id = id).delete()
    return redirect('/')


def deleteAll(request):
    Task.objects.all().delete()
    return redirect('/')


def renameTask(request, id):
    if request.method == "POST":
        task = Task.objects.get(id=id)
        task.task = request.POST['taskName']
        task.save()
        return redirect('/')

    return redirect("/")


def statusJustAdded(request, id):
    task = Task.objects.get(id=id)
    task.status = "Just Added"
    task.save()

    return redirect('/')

def statusPending(request, id):
    task = Task.objects.get(id=id)
    task.status = "Pending"
    task.save()

    return redirect('/')

def statusCompleted(request, id):
    task = Task.objects.get(id=id)
    task.status = "Completed"
    task.save()

    return redirect('/')

