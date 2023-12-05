from django.urls import path

from link_app.views import first_view, second_view, third_view

app_name = 'link_app'

urlpatterns = [
    path('one/', first_view, name='first_name'),
    path('second/', second_view, name='second_name'),
    path('third/<str:param>/', third_view, name='third_name'),
]