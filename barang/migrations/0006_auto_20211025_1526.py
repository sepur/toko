# Generated by Django 3.1.2 on 2021-10-25 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barang', '0005_auto_20211025_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemorder',
            name='harga_item',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='itemorder',
            name='total_item',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]