# Generated by Django 5.1 on 2024-08-11 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_alter_contactform_ride_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactform',
            name='passanger_count',
            field=models.CharField(blank=True, choices=[('one', '1'), ('two', '2'), ('three', '3'), ('four', '4'), ('one', '5'), ('six', '6')], default='one', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='ride_type',
            field=models.CharField(choices=[('comfort', 'Comfort'), ('van_comfort', 'Van Comfort'), ('black_limo', 'Black Limo')], default='1', max_length=20),
        ),
    ]
