# Generated by Django 2.1.2 on 2018-11-04 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_auto_20181104_1653'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='intern',
            name='prev_school_1',
        ),
        migrations.RemoveField(
            model_name='intern',
            name='prev_school_2',
        ),
    ]
