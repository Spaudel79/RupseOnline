# Generated by Django 2.2 on 2021-03-14 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20210314_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variants',
            name='product_id',
            field=models.CharField(blank=True, default='OAXWRTZ_12C', max_length=70),
        ),
    ]