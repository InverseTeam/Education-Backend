import json
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from users.models import *
from sections.models import *


ROOT_URL = 'https://inverse-tracker.ru'


class TestSectionApiTestCase(APITestCase):
    def setUp(self):
        self.school_class = Class.objects.create(number=9, litera='И')
        self.school = School.objects.create(name='МАОУ СОШ №215')
        self.school.classes.set([self.school_class.pk])
        self.role = Role.objects.create(role_name='Учитель', role_type='teacher')
        self.user = CustomUser.objects.create_user(email='inverse@mail.ru', role=self.role, school=self.school,
                                                   school_class=self.school_class, password='12345')
        self.client.force_authenticate(self.user)
        
        self.category = Category.objects.create(name='Технические предметы')

        self.section_json = {
            "name": "Программирование на Python",
            "description": "Прогроммируем на Python, подчиняя себе мир",
            "category": self.category.pk,
            "address": "Проспект Космонавтов 28",
            "rate": 4.5,
            "comments": 343,
            "groups": [{
                "name": "TK-3343",
                "teacher": 1,
                "total_students": 24,
                "max_students": 45,
                "schedules": [{
                    "week_day": "2",
                    "start_time": "12:00:00",
                    "end_time": "13:30:00"
                }]
            }]
        }

    def test_create_section(self):
        create_response = self.client.post(f'{ROOT_URL}/api/sections/create/', self.section_json)
        self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)

    def test_get_all_sections(self):
        craete_response = self.client.post(f'{ROOT_URL}/api/sections/create/', self.section_json)
        get_list_response = self.client.get(f'{ROOT_URL}/api/sections/')
        print(get_list_response.data)

        self.assertEqual(get_list_response.status_code, status.HTTP_200_OK)

    def test_get_section(self):
        create_response = self.client.post(f'{ROOT_URL}/api/sections/create/', self.section_json)
        get_detail_response = self.client.get(f'{ROOT_URL}/api/sections/{create_response.data["id"]}/')

        self.assertEqual(get_detail_response.status_code, status.HTTP_200_OK)

