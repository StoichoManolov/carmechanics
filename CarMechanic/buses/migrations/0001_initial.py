# Generated by Django 5.1.4 on 2024-12-17 23:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=20)),
                ('km', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Modifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('repair', models.CharField(max_length=200)),
                ('bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buses.bus')),
            ],
        ),
    ]