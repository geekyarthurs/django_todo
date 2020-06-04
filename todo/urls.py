from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='todo-app'),
    path('delete/<int:pk>', views.delete, name='delete-todo')
]
