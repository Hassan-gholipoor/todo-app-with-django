from django.urls import path
from . import views


app_name = 'todo'

urlpatterns = [
    path('', views.ShowTodo.as_view(), name='home'),
    path('detail/<slug:slug>', views.DetailTodo.as_view(), name='detail'),
    path('delete/<slug:slug>', views.DeleteTask.as_view(), name='delete'),
    path('add', views.AddTask.as_view(), name='add_task'),
    path('update/<slug:slug>', views.UpdateTodo.as_view(), name='update')
]