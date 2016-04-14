import copy
from django.test import TestCase
from django.contrib.auth.models import User
from app.models import Section
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate

test_section = Section(section="15F-CISC108021L: INTRO TO COMPUTER SCIENCE I, 15F-CISC108010: INTRO TO COMPUTER SCIENCE I")

test_user_1 = {
    'first_name': 'Henry',
    'last_name': 'Ford',
    'username': 'hford',
    'email': 'hford@udel.edu',
    'section': test_section.section,
    'password1': 'password123',
    'password2': 'password123',
}

test_user_2 = {
    'first_name': 'Wesley',
    'last_name': 'Weasle',
    'username': 'wweasle',
    'email': 'wweasle@udel.edu',
    'section': test_section.section,
    'password1': 'password123',
    'password2': 'password123',
}

def setup():
    test_section.save()



class RegisterStudentTest(TestCase):

    def test_standard_registration(self):
        """
        Test that a standard registration works.
        """
        setup()
        response = self.client.post(reverse('accounts:register_student'), test_user_1)
        self.assertRedirects(response, reverse('app:index'))
        user = authenticate(username=test_user_1['username'], password=test_user_1['password1'])
        self.assertEqual(user.username, test_user_1['username'])

    def test_non_udel_email(self):
        """
        If did not register with a udel.edu email, form should raise the error message
        'Must ues a udel.edu email.'
        """
        setup()
        gmail_user = copy.deepcopy(test_user_1)
        gmail_user['email'] = 'hford@gmail.com'
        response = self.client.post(reverse('accounts:register_student'), gmail_user)
        self.assertFormError(response, 'form', 'email', ['Must use a udel.edu email.'])

    def test_email_exists_error(self):
        """
        When a user attempts to register with an already used email, the form should
        raise an error message.
        """
        setup()
        same_email = copy.deepcopy(test_user_2)
        same_email['email'] = test_user_1['email']

        # Register first user
        self.client.post(reverse('accounts:register_student'), test_user_1)

        # Register second user
        response = self.client.post(reverse('accounts:register_student'), same_email)

        self.assertFormError(response, 'form', 'email', ['This email is already in use.'])
