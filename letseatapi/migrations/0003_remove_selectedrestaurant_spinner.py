# Generated by Django 4.1.3 on 2024-09-17 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('letseatapi', '0002_alter_user_profile_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='selectedrestaurant',
            name='spinner',
        ),
    ]
