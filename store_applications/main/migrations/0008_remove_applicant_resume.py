# Generated by Django 4.1.5 on 2023-01-29 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_applicant_resume'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicant',
            name='resume',
        ),
    ]
