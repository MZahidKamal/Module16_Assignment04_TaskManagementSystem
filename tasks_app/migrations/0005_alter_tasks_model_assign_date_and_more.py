# Generated by Django 5.0 on 2023-12-08 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks_app', '0004_rename_assigned_date_tasks_model_assign_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks_model',
            name='assign_date',
            field=models.DateTimeField(unique=True),
        ),
        migrations.AlterField(
            model_name='tasks_model',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
