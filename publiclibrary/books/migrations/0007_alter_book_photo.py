# Generated by Django 3.2.6 on 2021-09-03 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_alter_book_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to='images/'),
        ),
    ]
