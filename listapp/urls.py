from django.urls import path
from .views import task_list, task_detail, task_create, task_update, delete_view
from .api import TaskListAPI, TaskDetailAPI


urlpatterns=[
    #web views
    path('', task_list.as_view(), name='tasks'),
    path('task/<int:pk>/', task_detail.as_view(), name='task'),
    path('create-task/', task_create.as_view(), name='task-create'),
    path('create-update/<int:pk>/', task_update.as_view(), name='task-update'),
    path('delete/<int:pk>/', delete_view.as_view(), name='task-delete'),

    # API endpoints
    path('api/tasks/', TaskListAPI.as_view(), name='task-list-api'),
    path('api/tasks/<int:pk>/', TaskDetailAPI.as_view(), name='task-detail-api'),
]   

