from django.urls import path
# from material.admin.sites import site
from .views import (
    application_form,
    application_submit
    )

app_name = "membership"
urlpatterns = [
    path('', application_form, name="application_form"),
    path('submit/', application_submit, name="application_submit"),
]

