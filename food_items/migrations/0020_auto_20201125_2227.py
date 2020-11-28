# Generated by Django 3.1.3 on 2020-11-25 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_items', '0019_auto_20201125_2224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='itemperquantity',
        ),
        migrations.AddField(
            model_name='cart',
            name='itemperquantity',
            field=models.ManyToManyField(blank=True, null=True, related_name='itemperquantity', to='food_items.ItemPerQuantity'),
        ),
    ]
