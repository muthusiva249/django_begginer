# Generated by Django 4.2.6 on 2023-12-23 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_register', '0005_auto_20231223_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='salary',
            field=models.FloatField(default=10, max_length=15),
        ),
    ]
