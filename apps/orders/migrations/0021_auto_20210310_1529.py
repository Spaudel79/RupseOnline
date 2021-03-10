# Generated by Django 2.2 on 2021-03-10 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0020_orderitem_order_variants'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='start_date',
        ),
        migrations.AlterField(
            model_name='order',
            name='ordered_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
