# Generated by Django 2.2 on 2021-03-14 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_variants_product_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=-1),
            preserve_default=False,
        ),
    ]
