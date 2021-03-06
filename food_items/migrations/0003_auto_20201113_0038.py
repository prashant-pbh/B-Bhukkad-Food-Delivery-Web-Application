# Generated by Django 3.1.1 on 2020-11-12 19:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('food_items', '0002_auto_20201112_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='image',
            field=models.ImageField(blank=True, default='default_restaurant.png', upload_to=''),
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant_name', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('status', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='food_items.owner'),
        ),
    ]
