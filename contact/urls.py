from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='contact'),
  path('detail/<int:id>', views.detail, name='contact_detail'),
  path('update/<int:id>', views.update, name='contact_update'),
  path('create/', views.create, name='contact_create'),
  path('delete/<int:id>', views.delete, name='contact_delete'),
]