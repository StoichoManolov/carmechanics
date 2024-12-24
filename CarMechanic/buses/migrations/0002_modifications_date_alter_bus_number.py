# Generated by Django 5.1.4 on 2024-12-24 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='modifications',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bus',
            name='number',
            field=models.CharField(error_messages={'unique': 'Има бус с този номер!'}, max_length=20, unique=True),
        ),
    ]