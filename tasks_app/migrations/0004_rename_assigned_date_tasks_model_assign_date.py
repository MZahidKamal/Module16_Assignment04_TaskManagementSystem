# Generated by Django 5.0 on 2023-12-08 03:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks_app', '0003_remove_tasks_model_assign_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tasks_model',
            old_name='assigned_date',
            new_name='assign_date',
        ),
    ]
