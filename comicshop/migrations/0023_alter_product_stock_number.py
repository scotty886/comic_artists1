# Generated by Django 5.1.6 on 2025-03-17 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comicshop', '0022_alter_product_image_alter_product_image1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stock_number',
            field=models.CharField(max_length=6, verbose_name='eHBk9o'),
        ),
    ]
