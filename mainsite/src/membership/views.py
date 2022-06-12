from django.shortcuts import render, redirect
from .models import Application
from .forms import ApplicationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def application_form(request):
  if request.method == 'POST':
    form = ApplicationForm(request.POST)
    if form.is_valid():
      form.save()
      messages.info(request, 'Your application submitted successfully, we shall respond to your request via the your email as soon as possible')
      return redirect('membership:application_submit')

  
  form = ApplicationForm()

  context = {
    'form': form,
  }
  return render(request, 'membership/application.html', context)


def application_submit(request):
  
  return render(request, 'membership/application_submit.html')
