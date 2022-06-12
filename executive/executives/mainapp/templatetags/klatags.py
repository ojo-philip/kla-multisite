from django import template
from django.contrib import messages
from mainapp.forms import ContactForm
from django.shortcuts import redirect


register = template.Library()


@register.inclusion_tag("mainapp/contact.html")
def contact_tag(request):
  if request.method == "POST":
    form = ContactForm(request.POST)
    if form.is_valid():
      form.save()
      messages.info(request, 'You have successfully contacted us, we will respond via  email as soon as possible')
    


  form = ContactForm()
  
  return {
      "form": form,
        
    }