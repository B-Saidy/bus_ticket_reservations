# Generated by Django 2.2.4 on 2020-08-27 02:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_booking'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='passenger',
            new_name='user',
        ),
    ]