# Generated by Django 5.1.5 on 2025-02-14 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('multiagent', '0003_multiagent_an_model_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='multiagent',
            old_name='an_model_id',
            new_name='an_model',
        ),
    ]
