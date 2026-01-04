from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name='home'),
    path('task', views.task, name='task'),
    path('add_task', views.add_task, name='add_task'),
    path('delete/<int:task_id>/', views.complete_task, name='complete_task'),
    path('delete_task/<int:task_id>/', views.delete_task, name='deletetask'),

]

