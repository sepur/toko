# Generated by Django 3.1.2 on 2022-01-27 03:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('barang', '0008_auto_20220127_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stok',
            name='stok_barang',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barang.barang'),
        ),
    ]
