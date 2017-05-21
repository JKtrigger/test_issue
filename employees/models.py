# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.utils.translation import ugettext as _

from django.db import models

phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message=_(
        u'Номер телефона должен быть введен в формате: «+999999999». '
        u'Допускается до 15 цифр.'
    )
)


class PositionEnum(object):
    """
    Коллекция должностей
    """
    ADMINISTRATOR, ANALYST, AUDITOR, AUCTIONEER, STOCKBROKER = range(0, 5)
    TRADER, ACCOUNTANT, ACCOUNTANT_AUDITOR, DEALER, DISPATCHER = range(5, 10)
    DERMATOLOGIST, ENGINEER, BROKER = range(11, 14)

    values = {
        ADMINISTRATOR: _(u'Администратор'),
        ANALYST: _(u'Аналитик'),
        AUDITOR: _(u'Аудитор'),
        AUCTIONEER: _(u'Аукционист'),
        STOCKBROKER: _('Биржевой маклер'),
        TRADER: _('Биржевик'),
        ACCOUNTANT: _(u'Бухгалтер'),
        ACCOUNTANT_AUDITOR: _(u'Бухгалтер-аудитор'),
        DEALER: _(u'Дилер'),
        DISPATCHER: _(u'Диспетчер'),
        DERMATOLOGIST: _(u'Документовед'),
        ENGINEER: _(u'Инженер'),
        BROKER: _('Брокер'),
    }


class Department(models.Model):
    u"""
    Модель  отделов
    """
    code = models.CharField(max_length=30, null=True, blank=True)
    name = models.CharField(max_length=30, null=True, blank=True)

    def __unicode__(self):
        return self.name


class Employees(User):
    u"""
    Модель сотрудников
    """

    patronymic = models.CharField(
        _(u'Отчество'), max_length=30, null=True, blank=True
    )
    date_birth = models.DateField(_(u'Дата рождения'))
    employment_date = models.DateField(
        _(u'Дата приема на рабоу'), blank=True, null=True
    )
    date_of_dismissal = models.DateField(
        _(u'Дата увольнения'), blank=True, null=True
    )

    phone_number = models.CharField(
        max_length=15, validators=[phone_regex], blank=True
    )
    department = models.ForeignKey(
        Department, verbose_name=_(u'отдел'), null=True,
        blank=True, db_index=True
    )
    position = models.SmallIntegerField(
        choices=PositionEnum.values.items()
    )

    @property
    def fullname(self):
        return u' '.join(
            [
                self.last_name or u'',
                self.first_name or u'',
                self.patronymic or u''
             ]
        )

    @property
    def position_display(self):
        return PositionEnum.values.get(self.position, None)

    User._meta.get_field('first_name').verbose_name = _(u'Имя')
    User._meta.get_field('last_name').verbose_name = _(u'Фамилия')
    User._meta.get_field('is_staff').help_text = _(
        'Указывыет может ли полльзователь регистрироваться '
        'на административном ресурсе'
    )
    User._meta.get_field('is_active').help_text = _(
        'Указывыет является ли учетная запись действущей'
    )
