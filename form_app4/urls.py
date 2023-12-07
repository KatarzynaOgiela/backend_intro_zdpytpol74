from django.urls import path
from form_app4.views import task_create_view, task_list_view, task_detail_view

app_name = 'form_app4'


urlpatterns = [
    # C z crud
    path('tasks/create/', task_create_view, name='create_task'),

    # R z crud LISTA
    path('tasks/', task_list_view, name='list_task'),

    # R z crud SZCEGOL
    path('tasks/<int:task_id>/', task_detail_view, name='list_detail')
]