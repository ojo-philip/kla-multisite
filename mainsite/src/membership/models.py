from django.db import models

class Application(models.Model):
    UNIT_CHOICES = (
          ('Select one', 'Select one'),
          ('Content directorate', 'Content directorate'),
          ('Graphic design and videography directorate', 'Graphic design and videography directorate'),
          ('Human Resources directorate', 'Human Resources directorate'),
          ('Publicity and website directorate', 'Publicity and website directorate'),
          ('Special duty directorate', 'Special duty directorate'),
          ('Grant directorate', 'Grant directorate'),
          ('Finance directorate', 'Finance directorate'),
          ('Editorial directorate', 'Editorial directorate'),
          ('Others', 'Others')
      )
    ORGANIZATION_MEETING_CHOICES = (
      ('Select one', 'Select one'),
      ("Yes", "Yes"),
      ("No", "No")
    )
    MARITAL_CHOICES = (
      ('Select one', 'Select one'),
      ("Single", "Single"),
      ("Married", "Married"),
      ("Others", "Others")
    )
    POTENTIAL_EXECUTIVE_CHOICES = (
      ('Select one', 'Select one'),
      ("Yes", "Yes"),
      ("No", "No")
    )
    email = models.EmailField( max_length=254)
    surname = models.CharField( max_length=50)
    other_names = models.CharField( max_length=50)
    country = models.CharField("country and state of origin(e.g Nigeria/Oyo state)", max_length=250)
    course_of_study = models.CharField(max_length=200)
    level_of_study = models.CharField("level of study/profession", max_length=50)
    marital_status = models.CharField("Marital status", max_length=50, choices=MARITAL_CHOICES, default="Select one")
    your_whatsapp_number = models.CharField("Your WhatsApp number", max_length=50)
    date_of_birth = models.DateField( auto_now=False, auto_now_add=False)
    be_a_member = models.CharField("Why do you want to be a member of KLA?", max_length=200)
    organization_meeting = models.CharField( "The organization meeting holds 10am to 12noon every third Saturday of the month. Is that fine with you?",choices=ORGANIZATION_MEETING_CHOICES, max_length=50, default='Select one')
    potential_executive = models.CharField( "Every member is a potential executive whenever the need arises. Is that fine with you?", choices=POTENTIAL_EXECUTIVE_CHOICES, max_length=50, default='Select one')
    skill = models.CharField("What skill(s) do you have? There is no problem If you have none yet", max_length=200)
    leadership  = models.CharField("Kindly state any leadership experience you have had. There is no problem if you have none yet.", max_length=100)
    your_hobbies = models.CharField(max_length=100)
    unit = models.CharField("Which KLA directorate will you like to join?", choices=UNIT_CHOICES, max_length=50, default='Select one')




    
    class Meta:
        verbose_name = ("Application")
        verbose_name_plural = ("Applications")

    def __str__(self):
        return self.surname