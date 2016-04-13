from django import forms
from app.models import Student, Section
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

class StudentRegistrationForm(UserCreationForm):
    email = forms.EmailField(required = True)
    username = forms.CharField(required = True)
    first_name = forms.CharField(required = True)
    last_name = forms.CharField(required = True)
    section = forms.ChoiceField(required = True, choices=Section.get_available_choices())

    def clean_and_validate_email(self):
        email = self.cleaned_data['email']
        domain = email.split('@')[1]
        if domain != "udel.edu":
            raise forms.ValidationError("Must use a udel.edu email.")
        return email

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'section', 'password1', 'password2')

    def save(self, commit=True):
        student = Student()

        form_username = self.cleaned_data['username']
        form_email = self.clean_and_validate_email()
        form_password = self.cleaned_data['password1']
        form_first_name = self.cleaned_data['first_name']
        form_last_name = self.cleaned_data['last_name']
        section = Section.objects.get(section=self.cleaned_data['section'])

        if commit:
            # Note, we have to use create_user because
            # it automatically hashes the password.
            user = User.objects.create_user(
                username=form_username,
                email=form_email,
                password=form_password,
                first_name=form_first_name,
                last_name=form_last_name,
            )

            # Setup student row
            student.section = section
            student.user = user
            student.save()

            # Link user with student
            user.student = student
            user.save()
            user = authenticate(username=user.username, password=form_password)

        print(user)
        return user
