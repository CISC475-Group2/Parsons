from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

def validate_udel_email(email):
    domain = email.split('@')[1]
    if domain != "udel.edu":
        raise ValidationError("Must use a udel.edu email.")

def validate_email_taken(email):
    if email and User.objects.filter(email=email).count():
        raise ValidationError("This email is already in use.")
