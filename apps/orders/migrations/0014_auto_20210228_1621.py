# Generated by Django 2.2 on 2021-02-28 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_auto_20210228_1604'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='billingdetails',
            name='order',
        ),
        migrations.AddField(
            model_name='order',
            name='billing_details',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order', to='orders.BillingDetails'),
        ),
    ]
