# Generated by Django 4.0.4 on 2022-06-12 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='')),
                ('email', models.EmailField(max_length=254, verbose_name='')),
                ('subject', models.CharField(max_length=500, verbose_name='')),
                ('message', models.TextField(verbose_name='')),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
        ),
    ]