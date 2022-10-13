from django.shortcuts import render
from todolist.models import Task
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
import json
from django.core import serializers
from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
# Create your views here.

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_todolist = Task.objects.filter(user=request.user)
    context = {
        'todolist_data': data_todolist,
        'userName': request.user,
    }
    return render(request, "todolist.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

def create_task(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        create_task = Task(
            user = request.user,
            title = title,
            description = description,
        )
        create_task.save()
        return redirect('todolist:create_task')
    return render(request, 'createtask.html')

def delete_todo_list(request, id):
    itemList = Task.objects.filter(id=id)
    itemList.delete()
    return redirect('todolist:show_todolist')

def cek_status(request, id):
    todoListCheck = Task.objects.get(pk=id)
    if (todoListCheck.is_finished == False):
        todoListCheck.is_finished = True
    else:
        todoListCheck.is_finished = False
    todoListCheck.save()
    return redirect('todolist:show_todolist')

@login_required(login_url='/todolist/login/')
def show_json(request):
    todolist_item = Task.objects.all()
    return HttpResponse(serializers.serialize('json', todolist_item), content_type='application/json')

def add_todolist_ajax(request):
    title = request.POST.get('title')
    description = request.POST.get('description')
    add_todolist_ajax = Task(
        user = request.user,
        title = title,
        description = description,
    )
    add_todolist_ajax.save()
    return JsonResponse({"task": "new todolist"})

@csrf_exempt
def delete_todolist_ajax(request,id):
    task = Task.objects.filter(pk=id)   
    task.delete()
    return JsonResponse({"task": "clear todolist"})