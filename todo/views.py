from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AddTodo
from .models import Todo


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = AddTodo(request.POST)
        form.save()

    data = Todo.objects.all()
    form = AddTodo()
    return render(request, 'todo/index.html', {
        'form': form,
        'data': data,
    })


def delete(request, pk):

    Todo.objects.filter(pk=pk).delete()
    return redirect('todo-app')
