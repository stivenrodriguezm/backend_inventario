# Generated by Django 3.2.9 on 2022-10-25 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0025_stock_nombre_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='caja',
            name='subTipo',
            field=models.CharField(max_length=50, null=True, verbose_name='subTipo'),
        ),
        migrations.AddField(
            model_name='caja',
            name='valorCaja',
            field=models.BigIntegerField(null=True, verbose_name='valorCaja'),
        ),
    ]
