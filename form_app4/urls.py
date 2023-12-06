from django.urls import path
from form_app4.views import task_create_view, task_list_view

app_name = 'form_app4'


urlpatterns = [
    path('task/create/', task_create_view, name='create_task'),
    path('task/', task_list_view, name='list_task'),
]