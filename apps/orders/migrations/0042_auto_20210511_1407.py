# Generated by Django 2.2 on 2021-05-11 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0041_auto_20210509_2042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
        migrations.AddField(
            model_name='order',
            name='order_items',
            field=models.ManyToManyField(blank=True, null=True, to='orders.OrderItem'),
        ),
    ]
