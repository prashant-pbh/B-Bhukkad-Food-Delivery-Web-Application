# Generated by Django 3.1.3 on 2020-11-28 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food_items', '0054_customerorderhistory'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomerOrderHistory',
        ),
    ]