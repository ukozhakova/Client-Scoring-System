# Generated by Django 3.0.6 on 2020-05-18 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_regional_gcvp_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='internal_code',
        ),
    ]
