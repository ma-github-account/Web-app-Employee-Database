#-*- coding:utf-8 -*-

from django.urls import path, re_path
from . import views

# namespace
app_name = 'hr'

urlpatterns = [
    # Create an employee
    path('create/', views.EmployeeCreateView.as_view(), name='employee_create'),
    # Retrieve employee list
    path('', views.EmployeeListView.as_view(), name='employee_list'),
    # Retrieve single employee object
    re_path(r'^(?P<pk>\d+)/$', views.EmployeeDetailView.as_view(), name='employee_detail'),
    # Update an employee
    re_path(r'^(?P<pk>\d+)/update/$', views.EmployeeUpdateView.as_view(), name='employee_update'),
    # Delete an employee
    re_path(r'^(?P<pk>\d+)/delete/$', views.EmployeeDeleteView.as_view(), name='employee_delete')

    # # Create a task
    # path('create/', views.task_create, name='task_create'),
    # # Retrieve task list
    # path('', views.task_list, name='task_list'),
    # # Retrieve single task object
    # re_path(r'^(?P<pk>\d+)/$', views.task_detail, name='task_detail'),
    # # Update a task
    # re_path(r'^(?P<pk>\d+)/update/$', views.task_update, name='task_update'),
    # # Delete a task
    # re_path(r'^(?P<pk>\d+)/delete/$', views.task_delete, name='task_delete'),

]