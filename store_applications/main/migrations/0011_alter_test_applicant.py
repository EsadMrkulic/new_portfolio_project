# Generated by Django 4.1.5 on 2023-01-29 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_application_reviewed_by_manager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='applicant',
            field=models.ForeignKey(db_column='applicant_id', default=1, on_delete=django.db.models.deletion.CASCADE, to='main.applicant'),
        ),
    ]