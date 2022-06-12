from django.urls import path
# from material.admin.sites import site
from .views import (
    home_page,
    about_page,
    donation_page,
    our_executives,
    programs_page
    )

app_name = "main"
urlpatterns = [
    path('', home_page, name="home_page"),
    path('about-us/', about_page, name="about_page"),
    path('donation/', donation_page, name="donation_page"),
    path('our-executives/', our_executives, name="our_executives"),
    path('programs/', programs_page, name="programs_page"),
]

