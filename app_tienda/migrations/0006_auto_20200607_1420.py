# Generated by Django 2.1.3 on 2020-06-07 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_tienda', '0005_auto_20200607_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.IntegerField(default='', max_length=10),
        ),
    ]
