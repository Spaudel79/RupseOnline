# Generated by Django 2.2 on 2021-03-14 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_product_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variants',
            name='product_id',
            field=models.CharField(blank=True, default='OAXWRTZ_12C', max_length=70, null=True),
        ),
    ]
