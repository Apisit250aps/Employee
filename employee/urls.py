from django.urls import path
from . import views as api
urlpatterns = [
    path('employee', api.showEmployee, name='employee-api'),
    path('department', api.showDepartment, name='department-api'),
    path('employee-filter', api.EmployeeFilter, name='employee-filter-api'),
]