from django.contrib import admin
from .models import *

# Register your models here.
admin.site.site_header = "Kingdom Leads Africa Admin"


class EvaluationAdmin(admin.ModelAdmin):
  list_display = ("name", "directorate", "job", "reasons","attendance", "absent", "date" )

class DirectorateAdmin(admin.ModelAdmin):
  list_display = ("name", "plans_for_the_quarter", "resources_needed", "challenges_faced_in_the_previous_quarter","how_the_challenges_can_be_addressed")

admin.site.register(Evaluation, EvaluationAdmin)
admin.site.register(Directorate, DirectorateAdmin)

class ContactAdmin(admin.ModelAdmin):

  list_display = ["name", 'email', 'subject', 'message']
  list_filter = ["name", 'email', 'subject', 'message']

admin.site.register(Contact, ContactAdmin)