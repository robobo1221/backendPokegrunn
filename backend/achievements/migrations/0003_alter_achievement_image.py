# Generated by Django 4.2.6 on 2024-01-09 19:59

import achievements.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('achievements', '0002_achievement_qrcode_alter_achievement_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievement',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=achievements.models.upload_function),
        ),
    ]
