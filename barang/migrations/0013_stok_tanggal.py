# Generated by Django 3.1.2 on 2022-01-27 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barang', '0012_stok_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='stok',
            name='tanggal',
            field=models.DateField(blank=True, null=True),
        ),
    ]