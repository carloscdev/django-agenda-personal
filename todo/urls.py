from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='todo'),
  path('detail/<int:id>', views.detail, name='todo_detail'),
  path('update/<int:id>', views.update, name='todo_update'),
  path('create/', views.create, name='todo_create'),
  path('delete/<int:id>', views.delete, name='todo_delete'),
]