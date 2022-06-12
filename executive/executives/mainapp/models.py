from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Evaluation(models.Model):
  name = models.CharField( max_length=100) 
  directorate  = models.CharField( max_length=100) 
  job  = models.CharField("Job performed this month", max_length=400) 
  reasons  = models.CharField("Reason, if no job performed", max_length=400) 
  attendance  = models.CharField("Attendance at monthly meeting ", max_length=400) 
  absent  = models.CharField("Reason, if absent", max_length=400) 
  date = models.DateField(auto_now=True, auto_now_add=False)

  class Meta:
    verbose_name = "KLA Monthly Members and Executives Evaluation Sheet"
    verbose_name_plural = "KLA Monthly Members and Executives Evaluation Sheet"

  def __str__(self):
      return self.name
  


class Directorate(models.Model):
  name = models.CharField( max_length=100) 
  plans_for_the_quarter = models.TextField()
  resources_needed = models.TextField()
  challenges_faced_in_the_previous_quarter = models.TextField()
  how_the_challenges_can_be_addressed = models.TextField()


  class Meta:
    verbose_name = "Directorate's Quarterly Evaluation Form"
    verbose_name_plural = "Directorate's Quarterly Evaluation Form"

  def __str__(self):
      return self.name

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
  