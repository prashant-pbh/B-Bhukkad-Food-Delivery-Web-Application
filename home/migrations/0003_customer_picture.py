# Generated by Django 3.1.1 on 2020-11-10 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20201110_1854'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='picture',
            field=models.ImageField(default='default.png', upload_to=''),
        ),
    ]
