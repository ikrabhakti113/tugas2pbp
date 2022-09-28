from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from http.client import HTTPResponse
from todolist.models import mytodolistitem
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import datetime
from django.urls import reverse

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_todolist = mytodolistitem.objects.filter(user=request.user)
    context = {
    'list_task': data_todolist,
    }
    return render(request, "todolist.html", context)

def create_task(request):
    if request.method == "POST":
        is_finished = False
        mytodolistitem.objects.create(title=request.POST.get('title'), description=request.POST.get('description'), date=datetime.datetime.now(), user=request.user, is_finished=is_finished)
        response = HttpResponseRedirect(reverse('todolist:show_todolist'))
        return response
    return render(request, "create_task.html")

def delete(request, id):
  task = mytodolistitem.objects.get(id=id)
  task.delete()
  return HttpResponseRedirect(reverse('todolist:show_todolist'))

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

def check(request, update_status):
    check_status = mytodolistitem.objects.get(id=update_status)
    if check_status.is_finished == False:
        check_status.is_finished = True
    else:
        check_status.is_finished = False
    check_status.save()
    return HttpResponseRedirect(reverse('todolist:show_todolist'))

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










