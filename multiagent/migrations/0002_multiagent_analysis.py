# Generated by Django 5.1.5 on 2025-02-12 18:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0001_initial'),
        ('multiagent', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='multiagent',
            name='analysis',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='analysis.analysis'),
        ),
    ]
