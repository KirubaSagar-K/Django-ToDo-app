from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page = 'login'), name='logout'),
    path('register/', views.Register.as_view(), name='register'),

    path('', views.Tasklist.as_view(), name='tasks'),
    path('task/<int:pk>', views.Task_detail.as_view(), name='task-detail'),
    path('task-create/', views.Task_create.as_view(), name='task-create'),
    path('task-update/<int:pk>/', views.Task_update.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', views.Task_delete.as_view(), name='task-delete'),
]