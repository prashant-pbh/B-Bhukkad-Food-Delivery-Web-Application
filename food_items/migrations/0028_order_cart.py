# Generated by Django 3.1.3 on 2020-11-27 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food_items', '0027_order_pending'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cart',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='food_items.cart'),
        ),
    ]
