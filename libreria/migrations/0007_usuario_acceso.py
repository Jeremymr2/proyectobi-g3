# Generated by Django 4.2.2 on 2023-07-07 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0006_libro_precio'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='acceso',
            field=models.CharField(max_length=100, null=True, verbose_name='Tipo de acceso'),
        ),
    ]