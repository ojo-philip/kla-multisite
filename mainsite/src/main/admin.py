from django.contrib import admin
from .models import Event, Contact

admin.site.site_header = "Kingdom Leads Africa Admin"

class EventAdmin(admin.ModelAdmin):

  list_display = ["title", 'date', 'author', 'details']
  list_filter = ["title", 'date', 'author', 'details']

admin.site.register(Event, EventAdmin)

class ContactAdmin(admin.ModelAdmin):

  list_display = ["name", 'email', 'subject', 'message']
  list_filter = ["name", 'email', 'subject', 'message']

admin.site.register(Contact, ContactAdmin)
