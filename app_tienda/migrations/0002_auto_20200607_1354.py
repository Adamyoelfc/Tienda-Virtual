# Generated by Django 2.1.3 on 2020-06-07 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_tienda', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=225)),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='descripcion',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='producto',
            name='title',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='producto',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='app_tienda.Category'),
        ),
    ]