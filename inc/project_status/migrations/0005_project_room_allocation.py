# Generated by Django 4.2.6 on 2023-10-13 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_status', '0004_remove_project_id_alter_project_project_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='room_allocation',
            field=models.CharField(default='--null--', max_length=10),
        ),
    ]
