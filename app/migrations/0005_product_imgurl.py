# Generated by Django 5.0 on 2023-12-23 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_product_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='imgurl',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
