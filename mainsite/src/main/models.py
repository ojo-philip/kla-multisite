from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
  title = models.CharField(max_length=100)
  date = models.DateField(auto_now=False, auto_now_add=False)
  details = models.CharField(max_length=500)
  author = author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
  image = models.ImageField( upload_to="event-image")

  class Meta:
    verbose_name = 'Event'
    verbose_name_plural = 'Events'

  def __str__(self):
    return self.title


class Contact(models.Model):
  name = models.CharField("", max_length=100)
  email = models.EmailField("", max_length=254)
  subject = models.CharField("", max_length=500)
  message = models.TextField("")

  class Meta:
    verbose_name = 'Contact'
    verbose_name_plural = 'Contacts'

  def __str__(self):
    return self.name
