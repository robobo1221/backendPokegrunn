# Generated by Django 4.2.6 on 2024-01-10 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('achievements', '0004_alter_achievement_business_delete_business'),
    ]

    operations = [
        migrations.RenameField(
            model_name='achievement',
            old_name='langitude',
            new_name='latitude',
        ),
    ]
