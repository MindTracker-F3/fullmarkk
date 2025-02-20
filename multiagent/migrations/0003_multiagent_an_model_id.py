# Generated by Django 5.1.5 on 2025-02-14 18:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0003_analysis_rep_id'),
        ('multiagent', '0002_rename_vid_multiagent_videos'),
    ]

    operations = [
        migrations.AddField(
            model_name='multiagent',
            name='an_model_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='analysis.analysis'),
        ),
    ]
