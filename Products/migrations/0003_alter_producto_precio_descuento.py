# Generated by Django 5.1.4 on 2024-12-20 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0002_producto_precio_descuento_alter_producto_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio_descuento',
            field=models.FloatField(blank=True, null=True),
        ),
    ]