from django.test import TestCase
from .models import Member

class MemberModelTest(TestCase):
    def test_string_representation(self):
        member = Member(id=17, firstname='Faye', lastname='King', phone=5551234567, joined_date='2024-10-07')
        self.assertEqual(str(member), '[017] Faye King')

class HomeViewTest(TestCase):
    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

class MemberViewTest(TestCase):
    def test_when_list_is_empty(self):
        response = self.client.get('/members/')
        self.assertEqual(response.status_code, 200)