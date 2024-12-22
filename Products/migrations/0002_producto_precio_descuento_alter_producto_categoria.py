# Generated by Django 5.1.4 on 2024-12-20 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='precio_descuento',
            field=models.FloatField(default=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.CharField(choices=[('Cl', 'Clothes'), ('Ac', 'Accesories'), ('El', 'Electronics'), ('Sp', 'Sports'), ('Bk', 'Books'), ('Fd', 'Foods')], max_length=2),
        ),
    ]