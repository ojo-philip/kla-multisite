from django.urls import path
from .views import (
  evaluation_form,
  directorate_form,
  executives_page,
  application_submit
)

app_name = "mainapp"
urlpatterns = [
    path('', executives_page, name="executives_page"),
    path('evaluation/', evaluation_form, name="evaluation_form"),
    path('directorate/', directorate_form, name="directorate_form"),
    path('application-submit/', application_submit, name="application_submit"),
]
