# Generated by Django 3.1.1 on 2020-11-10 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='created',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='updated',
        ),
    ]
