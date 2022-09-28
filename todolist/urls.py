from todolist.views import register
from todolist.views import show_todolist
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import create_task
from todolist.views import delete
from todolist.views import check
from django.urls import path

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create_task/', create_task, name='create_task'),
    path('delete/<int:id>', delete, name='delete'),
    path('check/<int:update_status>', check, name='check'),
]



