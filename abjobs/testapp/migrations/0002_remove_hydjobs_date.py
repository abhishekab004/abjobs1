# Generated by Django 4.1.7 on 2023-06-26 06:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hydjobs',
            name='date',
        ),
    ]
