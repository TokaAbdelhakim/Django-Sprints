# Generated by Django 3.2.6 on 2021-09-04 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_product_show'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='show',
            field=models.DecimalField(decimal_places=0, default=1, max_digits=1),
        ),
    ]
