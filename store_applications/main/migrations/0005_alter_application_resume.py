# Generated by Django 4.1.5 on 2023-01-29 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_application_reviewed_by_manager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='resume',
            field=models.FileField(upload_to='files/'),
        ),
    ]
