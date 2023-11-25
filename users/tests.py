from django.test import TestCase
from django.contrib.auth import get_user_model
from users.models import *


# class SignInViewTest(TestCase):
#     def setUp(self):
#         # self.role = Role.objects.create(role_name='Ученик', role_type='student')
#         # self.school_class = Class.objects.create(number='9', litera='И')
#         # self.school = School.objects.create(name='Школа №215')

#         self.user = get_user_model().objects.create(email='ivan@mail.ru', firstname='Ivan', lastname='Belogurov', 
#                                               surname='Dmitrievich', password='12345')

        
#     def tearDown(self):
#         self.user.delete()

#     def test_correct(self):
#         response = self.client.post('/api/users/auth/token/login/', {
#             'email': 'ivan@mail.ru',
#             'password': '12345'})
        
#         self.assertTrue(response.data['authenticated'])