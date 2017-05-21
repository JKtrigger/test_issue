# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.contrib import admin
from django import forms

from employees.models import Employees, Department


class EmployeesForm(forms.ModelForm):
    class Meta:
        model = Employees
        exclude = ['name']


class EmployeesAdmin(admin.ModelAdmin):
    fields = (
        'first_name', 'last_name', 'patronymic', 'date_birth',
        'employment_date', 'date_of_dismissal',
        'phone_number', 'department', 'position',
        'username', 'password', 'email',
        'is_staff', 'is_active'
    )

    form = EmployeesForm


admin.site.register(Department)
admin.site.register(Employees, EmployeesAdmin)