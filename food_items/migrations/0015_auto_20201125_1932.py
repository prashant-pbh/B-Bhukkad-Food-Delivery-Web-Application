# Generated by Django 3.1.3 on 2020-11-25 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_items', '0014_cart_itemperquantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='itemperquantity',
            field=models.ManyToManyField(blank=True, default=True, null=True, related_name='itemperquantity', to='food_items.ItemPerQuantity'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='total',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=50000),
        ),
    ]
