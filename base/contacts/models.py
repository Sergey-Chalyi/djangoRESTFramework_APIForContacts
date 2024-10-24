import re
from django.core.exceptions import ValidationError
from django.db import models

# validator for field in model with phone number 
def validate_phone_number(phone_number):
    """
    Validates the phone number.

    Parameters:
    phone_number (str): The phone number to be validated.

    Raises:
    ValidationError: If the phone number does not start with '+' and contain only numbers.

    Returns:
    None
    """
    if not re.match(r'^\+\d+$', phone_number):
        raise ValidationError('Phone number must start with + and contain only numbers.')

# model
class Contact(models.Model):
    """
    A model representing a contact with first name, last name, phone number, and email.

    Attributes:
    first_name (CharField): The first name of the contact.
    last_name (CharField): The last name of the contact.
    phone_number (CharField): The phone number of the contact. Must be unique and start with '+'.
    email (EmailField): The email of the contact. Must be unique.

    Methods:
    __str__(): Returns a string representation of the contact in the format 'first_name_last_name'.
    save(*args, **kwargs): Validates the contact before saving it to the database.
    """

    first_name = models.CharField(max_length=255, null=False, blank=False)
    last_name = models.CharField(max_length=255, null=False, blank=False)
    phone_number = models.CharField(max_length=255, null=False, blank=False, unique=True, validators=[validate_phone_number])
    email = models.EmailField(max_length=255, null=False, blank=False, unique=True)

    def __str__(self):
        """
        Returns a string representation of the contact.

        Returns a string of the format 'first_name_last_name'.

        Returns:
        str: A string representation of the contact.
        """
        return f'{self.first_name}_{self.last_name}'

    def save(self, *args, **kwargs):
        """
        Validates the contact before saving it to the database.

        Parameters:
        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments.

        Returns:
        None
        """
        self.full_clean()
        super().save(*args, **kwargs)