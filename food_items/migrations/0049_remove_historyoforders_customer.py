# Generated by Django 3.1.3 on 2020-11-28 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food_items', '0048_historyoforders'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historyoforders',
            name='customer',
        ),
    ]
