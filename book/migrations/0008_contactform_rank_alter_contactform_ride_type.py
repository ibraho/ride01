# Generated by Django 5.1 on 2024-08-13 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_contactform_passanger_count_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactform',
            name='rank',
            field=models.IntegerField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='ride_type',
            field=models.CharField(choices=[('2.3', 'Comfort'), ('2.6', 'Van Comfort'), ('3.1', 'Black Limo')], default='1', max_length=20),
        ),
    ]
