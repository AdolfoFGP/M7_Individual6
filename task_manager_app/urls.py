from django.urls import path
from . import views

app_name = 'task_manager_app'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('welcome/', views.welcome_view, name='welcome'),
    path('tasks-list/', views.task_list_view, name='task_list'),
    path('register/', views.register_view, name='register'),
    path('task/create/', views.task_create_view, name='task_create'),
    path('task/<int:task_id>/delete/', views.task_delete_view, name='task_delete'),
    path('task/<int:pk>/', views.task_detail_view, name='task_detail'),
    path('task/<int:pk>/edit/', views.task_edit_view, name='task_edit'),
    path('task/<int:pk>/complete/', views.task_complete_view, name='task_complete'),
]

    
