# Generated by Django 5.1 on 2024-08-13 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0008_contactform_rank_alter_contactform_ride_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactform',
            old_name='rank',
            new_name='price',
        ),
    ]
