# Generated by Django 5.1.4 on 2024-12-24 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buses', '0002_modifications_date_alter_bus_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='modifications',
            old_name='bus',
            new_name='session',
        ),
        migrations.RemoveField(
            model_name='modifications',
            name='date',
        ),
    ]