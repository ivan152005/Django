# Generated by Django 5.1.4 on 2025-02-21 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('virgenDB', '0004_remove_usuario_metodos_pago_metodos_pago_id_usuario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pago_con_tarjeta',
            name='predeterminado',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='paypal',
            name='predeterminado',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='transferencia_bancaria',
            name='predeterminado',
            field=models.BooleanField(),
        ),
    ]
