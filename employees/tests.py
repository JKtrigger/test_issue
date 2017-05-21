# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.test import TestCase

from employees.models import Employees


class GenericViewTestCase(TestCase):

    def setUp(self):
        self.item = Employees.objects.create(
            first_name=u'Алекса́ндр',
            last_name=u'Попо́в',
            patronymic=u'Степа́нович',
            date_birth=datetime.date(1859,3,16),
            username=u'Alex',
            password=u'radio',
            email=u'popov@great_scientist.com',
            position=100
        )


class TestUrls(GenericViewTestCase):

    def test_pages(self):

        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/1')
        self.assertEqual(response.status_code, 200)
