# -*- coding:utf-8 -*-
import string

import datetime
import rstr
import random

from django.core.management.base import BaseCommand, CommandError
from django.utils.translation import ugettext as _

from employees.models import Employees, PositionEnum, Department


def random_date(start, end):
    return start + datetime.timedelta(
        seconds=random.randint(0, int((end - start).total_seconds())),
    )


class CustomCommandError(CommandError):
    message = _(u'Не более 300 за раз')

    def __init__(self):
        super(CustomCommandError, self).__init__(self.message)


class Command(BaseCommand):
    u"""
    Комманда заполнения данными

    использование:
    python manage.py fill_data_base --count {количество записей}
    """
    help = u'Команда заполняет таблицу model:`employees.models.Employees`'

    def add_arguments(self, parser):
        u""" Добавление аргумента count """
        parser.add_argument(
            u'--count', type=int,
            help=_(u'Количество записей. \n Не больше 300')
        )

    def handle(self, *args, **options):
        u""" Заполнение данных по шаблону """

        try:
            count = options['count']
            assert count <= 300
        except AssertionError:
            raise CustomCommandError

        departments = Department.objects.all()

        for i in xrange(0, count):
            first_name = rstr.rstr(u'АБВГДЕЗИКЛМНОПРСТУФХЭЮЯ',
                                   random.randint(4, 16))
            last_name = rstr.rstr(u'АБВГДЕЗИКЛМНОПРСТУФХЭЮЯ',
                                  random.randint(4, 16))

            self.stdout.write(
                u'Добавление :{} {}'.format(first_name, last_name))

            #  TODO: Can't bulk create a multi-table inherited model
            Employees(
                first_name=first_name,
                last_name=last_name,
                date_birth=datetime.datetime.today(),
                phone_number='+'+rstr.rstr('1234567890', 12),
                department=random.choice(departments),
                employment_date=random_date(
                    datetime.date(1999, 12, 12), datetime.date(2017, 01, 01)),
                date_of_dismissal=random_date(
                    datetime.date(2017, 01, 01), datetime.date(2050, 01, 01)),
                position=random.randint(
                    PositionEnum.ADMINISTRATOR, PositionEnum.BROKER),
                username=first_name+'_'+last_name,
                password=rstr.rstr(
                        string.ascii_uppercase + string.digits, 10),
                email=first_name + '@employee.com'


            ).save()

        self.stdout.write(u'{} записей было добавлено'.format(count))

