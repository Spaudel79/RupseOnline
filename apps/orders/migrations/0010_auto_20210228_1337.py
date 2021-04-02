# Generated by Django 2.2 on 2021-02-28 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_billingdetails_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billingdetails',
            name='order',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='billing_details', to='orders.Order'),
        ),
    ]
