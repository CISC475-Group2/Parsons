from django.test import TestCase
from django.contrib.auth.models import User
from app.models import Section
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate

class RegisterStudentTest(TestCase):

    def test_standard_registration(self):
        test_section = Section(section="15F-CISC108021L: INTRO TO COMPUTER SCIENCE I, 15F-CISC108010: INTRO TO COMPUTER SCIENCE I")
        test_section.save()

        test_user = {
            'first_name': 'Henry',
            'last_name': 'Ford',
            'username': 'hford',
            'email': 'hford@udel.edu',
            'section': test_section.section,
            'password1': 'password123',
            'password2': 'password123',
        }

        response = self.client.post(reverse('accounts:register_student'), test_user)
        self.assertRedirects(response, reverse('app:index'))
        user = authenticate(username=test_user['username'], password=test_user['password1'])
        self.assertEqual(user.username, test_user['username'])

    def test_non_udel_email(self):
        test_section = Section(section="15F-CISC108021L: INTRO TO COMPUTER SCIENCE I, 15F-CISC108010: INTRO TO COMPUTER SCIENCE I")
        test_section.save()

        test_user = {
            'first_name': 'Henry',
            'last_name': 'Ford',
            'username': 'hford',
            'email': 'hford@gmail.com',
            'section': test_section.section,
            'password1': 'password123',
            'password2': 'password123',
        }

        response = self.client.post(reverse('accounts:register_student'), test_user)
        self.assertRedirects(response, reverse('app:index'))
        user = authenticate(username=test_user['username'], password=test_user['password1'])
        self.assertEqual(user.username, test_user['username'])

