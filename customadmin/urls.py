from django.urls import path
from .views import *

urlpatterns = [
    path('signin/',admin_login,name='admin-login'),
    path('users/',get_users,name='get-users'),
    path('users/delete/<int:user_id>',delete_user,name='delete-user'),
    path('tasks/',get_tasks,name='tasks'),
    path('task/detail/<int:task_id>',get_task_detail,name='task-detail'),
    path('task/add',add_task,name='add-task')

]