# Generated by Django 5.1.5 on 2025-02-12 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0002_report_multiagent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='multiagent',
        ),
    ]
