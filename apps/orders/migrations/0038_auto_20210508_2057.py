# Generated by Django 2.2 on 2021-05-08 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0037_order_current_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='current_points',
            field=models.FloatField(default=0),
        ),
    ]
