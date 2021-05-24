# Generated by Django 2.2 on 2021-05-16 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0045_coupons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupons',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='coupons',
            name='discount',
            field=models.IntegerField(default=0),
        ),
    ]