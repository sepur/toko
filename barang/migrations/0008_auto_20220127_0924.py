# Generated by Django 3.1.2 on 2022-01-27 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barang', '0007_itemorder_total_harga_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stok',
            name='ukuran',
        ),
        migrations.AddField(
            model_name='barang',
            name='harga_jual',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='barang',
            name='jumlah_stok',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='itemorder',
            name='harga_barang',
            field=models.FloatField(blank=True, null=True),
        ),
    ]