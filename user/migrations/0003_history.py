# Generated by Django 5.1.5 on 2025-02-15 19:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_customuser_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition_name', models.JSONField(default=list)),
                ('diagnosis_date', models.DateField(auto_now_add=True)),
                ('current_status', models.CharField(default='Unknown', max_length=255)),
                ('userHistory_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='histories', to='user.customuser')),
            ],
        ),
    ]
