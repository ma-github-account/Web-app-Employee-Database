from django.contrib import admin
from hr.models import Employee


class EmployeeAdmin(admin.ModelAdmin):
  model = Employee
  list_display = ('employee_id', 'first_name','last_name')
  search_fields = ['employee_id']

# Register your models here.
admin.site.register(Employee)