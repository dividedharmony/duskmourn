from django.test import TestCase
from .models import Member

class MemberModelTest(TestCase):
    def test_string_representation(self):
        member = Member(id=17, firstname='Faye', lastname='King', phone=5551234567, joined_date='2024-10-07')
        self.assertEqual(str(member), '[017] Faye King')
