# Generated by Django 5.1 on 2024-08-11 17:44

import django.core.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_alter_contactform_ride_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactform',
            name='pick_up_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True, validators=[django.core.validators.EmailValidator()]),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='flight_nr',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='ride_type',
            field=models.CharField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)], default='1', max_length=20),
        ),
    ]
