# Generated by Django 5.1.5 on 2025-02-12 20:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0001_initial'),
        ('multiagent', '0003_remove_multiagent_analysis_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='analysis',
            name='id',
        ),
        migrations.AddField(
            model_name='analysis',
            name='model_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='analysis',
            name='multiAgent_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='multiagent.multiagent'),
        ),
    ]
