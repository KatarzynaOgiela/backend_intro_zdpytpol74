from django.urls import path
from form_app4 import views

app_name = 'form_app4'


urlpatterns = [
    # C z crud
    path('tasks/create/', views.task_create_view, name='task_create'),

    # R z crud LISTA
    path('tasks/', views.task_list_view, name='task_list'),

    # R z crud SZCEGOL
    path('tasks/<int:task_id>/', views.task_detail_view, name='task_detail'),

    # U
    path('tasks/<int:task_id>/update', views.task_update_view, name='task_update'),
    # D
    path('tasks/<int:task_id>/delete', views.task_delete_view, name='task_delete')
]