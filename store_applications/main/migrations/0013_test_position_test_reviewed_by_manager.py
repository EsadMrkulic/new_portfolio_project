# Generated by Django 4.1.5 on 2023-01-29 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_application_applicant_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='position',
            field=models.ForeignKey(db_column='position_id', default=1, on_delete=django.db.models.deletion.CASCADE, to='main.position'),
        ),
        migrations.AddField(
            model_name='test',
            name='reviewed_by_manager',
            field=models.ForeignKey(db_column='reviewed_by_manager_id', default=1, on_delete=django.db.models.deletion.CASCADE, to='main.manager'),
        ),
    ]