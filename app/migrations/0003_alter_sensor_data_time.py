# Generated by Django 4.2.2 on 2024-08-16 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_sensor_data_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor_data',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
