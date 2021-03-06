# Generated by Django 3.1.2 on 2021-10-25 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barang', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='barang',
            name='harga_barang',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='itemorder',
            name='ket_item',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='sts_bayar',
            field=models.CharField(blank=True, choices=[('1', 'BELUM'), ('2', 'LUNAS')], max_length=500, null=True),
        ),
    ]
