from django.shortcuts import render, redirect
from rest_framework import generics, permissions

from contacts.models import Contact
from contacts.serializers import ContactSerializer

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


class ContactsAPIViews(generics.ListCreateAPIView):
    """
    This class-based view provides a list of all contacts and allows creating new contacts.

    It uses Django's built-in `ListCreateAPIView` to handle GET and POST requests.

    Attributes:
        queryset (QuerySet): A QuerySet that retrieves all instances of the `Contact` model.
        serializer_class (ContactSerializer): A serializer class that converts the model instance data to native Python data types and vice versa.
        permission_classes (List[permissions.BasePermission]): A list of permission classes that restrict access to the API view.

    Args:
        queryset (QuerySet, optional): A QuerySet that retrieves all instances of the `Contact` model. Defaults to `Contact.objects.all()`.
        serializer_class (ContactSerializer, optional): A serializer class that converts the model instance data to native Python data types and vice versa. Defaults to `ContactSerializer`.
        permission_classes (List[permissions.BasePermission], optional): A list of permission classes that restrict access to the API view. Defaults to `[permissions.IsAuthenticated]`.

    Returns:
        Response: A JSON response containing a list of all contacts or a newly created contact.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]


class ContactDetailAPIViews(generics.RetrieveUpdateDestroyAPIView):
    """
    This class-based view provides a detailed view of a single contact, allows updating the contact's information, and deleting the contact.

    It uses Django's built-in `RetrieveUpdateDestroyAPIView` to handle GET, PUT, and DELETE requests.

    Attributes:
        queryset (QuerySet): A QuerySet that retrieves all instances of the `Contact` model. Defaults to `Contact.objects.all()`.
        serializer_class (ContactSerializer): A serializer class that converts the model instance data to native Python data types and vice versa. Defaults to `ContactSerializer`.
        permission_classes (List[permissions.BasePermission]): A list of permission classes that restrict access to the API view. Defaults to `[permissions.IsAuthenticated]`.

    Args:
        queryset (QuerySet, optional): A QuerySet that retrieves all instances of the `Contact` model.
        serializer_class (ContactSerializer, optional): A serializer class that converts the model instance data to native Python data types and vice versa.
        permission_classes (List[permissions.BasePermission], optional): A list of permission classes that restrict access to the API view.

    Returns:
        Response: A JSON response containing the detailed information of a single contact, updated contact information, or a confirmation message after deleting the contact.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]


def login(request):
    return render(request, 'login.html')


@login_required
def home(request):
    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    return redirect('login')