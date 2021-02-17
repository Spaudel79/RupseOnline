# Generated by Django 2.2 on 2021-02-17 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('orders', '0003_auto_20210217_1319'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlistitems',
            name='item',
        ),
        migrations.AddField(
            model_name='wishlistitems',
            name='item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Product'),
        ),
    ]
