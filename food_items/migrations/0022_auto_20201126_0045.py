# Generated by Django 3.1.3 on 2020-11-25 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_items', '0021_itemperquantity_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemperquantity',
            name='itemtotal',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='cart',
            name='total',
            field=models.FloatField(default=0.0),
        ),
    ]