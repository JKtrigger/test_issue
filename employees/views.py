# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import datetime

from django.db.models import Q
from django.views.generic import DetailView
from django.views.generic import ListView


from employees.models import Employees


class SectionListView(ListView):
    u"""
    Список работников
    """
    model = Employees
    paginate_by = 10
    groups = ['А-Г', 'Д-З', 'И-М', 'Н-Р', 'С-Ф', 'Х-Ш','Щ-Я']

    def get_context_data(self, **kwargs):
        context = super(SectionListView, self).get_context_data(**kwargs)
        context['groups'] = self.groups
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request.GET
        group_num = request.get('group_num', None)
        is_active = request.get('is_active', None)
        depart = request.get('depart', None)
        is_active_condition = Q()
        group_num_condition = Q()
        depart_condition = Q()
        if group_num and hash(group_num) != hash(u'None'):

            group_num_condition = Q(
                last_name__regex=r'^[{}].+'.format(self.groups[int(group_num)])
            )
        if is_active and hash(is_active) != hash(u'None'):

            if hash(is_active) == hash(u'True'):
                is_active_condition = Q(
                    date_of_dismissal__gt=datetime.date.today()
                )
            elif hash(is_active) == hash(u'False'):
                is_active_condition = Q(
                    date_of_dismissal__lte=datetime.date.today()
                )
        if depart and hash(depart) != hash(u'None'):
            depart_condition = Q(department__name__exact=depart)

        try:

            return Employees.objects.filter(
                is_active_condition,
                group_num_condition,
                depart_condition
            )

        except ValueError:
            pass

        return Employees.objects.all()

    def get(self, request, *args, **kwargs):
        return super(SectionListView, self).get(request, *args, **kwargs)


class EmployeesDetailView(DetailView):
    u"""
    Карточка Работника
    """
    model = Employees

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=self.model.objects.all())
        return super(EmployeesDetailView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(EmployeesDetailView, self).get_context_data(**kwargs)
        return context
