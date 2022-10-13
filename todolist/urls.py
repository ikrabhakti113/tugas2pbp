from django.urls import path
from todolist.views import add_todolist_ajax, show_json, show_todolist
from todolist.views import register
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import create_task
from todolist.views import delete_todo_list
from todolist.views import cek_status
from todolist.views import delete_todolist_ajax


app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create_task'),
    path('delete_todo_list/<int:id>/', delete_todo_list, name='delete_todo_list'),
    path('cek_status/<int:id>/', cek_status, name='cek_status'),
    path('json/', show_json , name='show_json'),
    path('add/', add_todolist_ajax , name='add_todolist_ajax'),
    path('delete/<int:id>/', delete_todolist_ajax, name='delete_todolist_ajax'),
]