# Generated by Django 2.2 on 2021-04-18 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_auto_20210404_1301'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_image_1', models.ImageField(blank=True, upload_to='banners/images')),
                ('banner_image_2', models.ImageField(blank=True, upload_to='banners/images')),
                ('banner_image_3', models.ImageField(blank=True, upload_to='banners/images')),
                ('square_image_1', models.ImageField(blank=True, upload_to='banners/images')),
                ('square_image_2', models.ImageField(blank=True, upload_to='banners/images')),
                ('square_image_3', models.ImageField(blank=True, upload_to='banners/images')),
            ],
            options={
                'verbose_name_plural': 'Banner Images',
            },
        ),
    ]
