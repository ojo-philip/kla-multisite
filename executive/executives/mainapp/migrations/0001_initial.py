# Generated by Django 4.0.4 on 2022-06-12 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Directorate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('plans_for_the_quarter', models.TextField()),
                ('resources_needed', models.TextField()),
                ('challenges_faced_in_the_previous_quarter', models.TextField()),
                ('how_the_challenges_can_be_addressed', models.TextField()),
            ],
            options={
                'verbose_name': "Directorate's Quarterly Evaluation Form",
                'verbose_name_plural': "Directorate's Quarterly Evaluation Form",
            },
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('directorate', models.CharField(max_length=100)),
                ('job', models.CharField(max_length=400, verbose_name='Job performed this month')),
                ('reasons', models.CharField(max_length=400, verbose_name='Reason, if no job performed')),
                ('attendance', models.CharField(max_length=400, verbose_name='Attendance at monthly meeting ')),
                ('absent', models.CharField(max_length=400, verbose_name='Reason, if absent')),
                ('date', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'KLA Monthly Members and Executives Evaluation Sheet',
                'verbose_name_plural': 'KLA Monthly Members and Executives Evaluation Sheet',
            },
        ),
    ]