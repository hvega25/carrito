# Generated by Django 4.2.1 on 2023-05-15 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carrito_app', '0003_rename_stock_producto_cantidad_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='envio',
            new_name='metodo_envio',
        ),
    ]