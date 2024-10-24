from rest_framework import serializers
from contacts.models import Contact


class ContactSerializer(serializers.ModelSerializer):
    """
    Serializer for the Contact model.

    This serializer is used to convert the Contact model data into JSON format for API responses.

    Args:
    - model (Contact): The model to be serialized.
    - fields (str): All fields of the model are included in the serialization.

    Returns:
    - serializer (ContactSerializer): An instance of the ContactSerializer class.
    """
    class Meta:
        model = Contact
        fields = '__all__'