# Generated by Django 3.1.2 on 2022-01-27 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barang', '0011_auto_20220127_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='stok',
            name='status',
            field=models.CharField(blank=True, choices=[('1', 'Waiting'), ('2', 'Approved')], max_length=500, null=True),
        ),
    ]
