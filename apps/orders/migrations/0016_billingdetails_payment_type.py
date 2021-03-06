# Generated by Django 2.2 on 2021-03-02 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0015_auto_20210301_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='billingdetails',
            name='payment_type',
            field=models.CharField(blank=True, choices=[('cash_on_delivery', 'Cash On Delivery'), ('credit/debit_card', 'Credit/Debit Card'), ('connect_ips', 'Connect IPS'), ('fonepay', 'Fonepay')], default='cash_on-delivery', max_length=50, null=True),
        ),
    ]
