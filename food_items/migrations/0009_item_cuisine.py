# Generated by Django 3.1.1 on 2020-11-19 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_items', '0008_auto_20201117_1219'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='cuisine',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]