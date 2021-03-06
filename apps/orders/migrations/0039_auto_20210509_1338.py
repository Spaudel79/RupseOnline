# Generated by Django 2.2 on 2021-05-09 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0038_auto_20210508_2057'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='points',
            name='points_gained',
            field=models.FloatField(default=0),
        ),
    ]
