# Generated by Django 3.2.6 on 2021-09-04 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_show'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='show',
            field=models.IntegerField(default=1),
        ),
    ]
