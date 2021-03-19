# Generated by Django 2.2 on 2021-03-15 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0023_auto_20210314_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('To_Ship', 'To Ship'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')], default='To_Ship', max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='total_item_price',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
