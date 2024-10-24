from django.contrib import admin

from contacts.models import Contact

# make the model be visible in admin panel
admin.site.register(Contact)
