import re
from django.core.exceptions import ValidationError
from django.db import models


def validate_phone_number(phone_number):
    if not re.match(r'^\+\d+$', phone_number):
        raise ValidationError('Phone number must start with + and contain only numbers.')


class Contact(models.Model):
    first_name = models.CharField(max_length=255, null=False, blank=False)
    last_name = models.CharField(max_length=255, null=False, blank=False)
    phone_number = models.CharField(max_length=255, null=False, blank=False, unique=True, validators=[validate_phone_number])
    email = models.EmailField(max_length=255, null=False, blank=False, unique=True)


    def __str__(self):
        return f'{self.first_name}_{self.last_name}'


    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)