# Generated by Django 5.0 on 2023-12-24 14:27

import builtins
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_product_categories'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=255)),
                ('subject', models.TextField()),
                ('message', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='confirmpassword',
            field=models.TextField(default=1, verbose_name=builtins.hash),
            preserve_default=False,
        ),
    ]