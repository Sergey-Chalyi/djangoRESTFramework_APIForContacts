from django.shortcuts import render
from rest_framework import generics, permissions

from contacts.models import Contact
from contacts.serializers import ContactSerializer


class ContactsAPIViews(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]


class ContactDetailAPIViews(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]
