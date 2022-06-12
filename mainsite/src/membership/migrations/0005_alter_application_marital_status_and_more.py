# Generated by Django 4.0.4 on 2022-06-02 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0004_application_country_application_marital_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='marital_status',
            field=models.CharField(choices=[('Select one', 'Select one'), ('Single', 'Single'), ('Married', 'Married'), ('Others', 'Others')], default='Select one', max_length=50, verbose_name='Marital status'),
        ),
        migrations.AlterField(
            model_name='application',
            name='unit',
            field=models.CharField(choices=[('Select one', 'Select one'), ('Content directorate', 'Content directorate'), ('Graphic design and videography directorate', 'Graphic design and videography directorate'), ('Human Resources directorate', 'Human Resources directorate'), ('Publicity and website directorate', 'Publicity and website directorate'), ('Special duty directorate', 'Special duty directorate'), ('Grant directorate', 'Grant directorate'), ('Finance directorate', 'Finance directorate'), ('Editorial directorate', 'Editorial directorate'), ('Others', 'Others')], default='Select one', max_length=50, verbose_name='Which KLA directorate will you like to join?'),
        ),
    ]
