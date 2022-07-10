# Generated by Django 4.0 on 2022-02-02 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Computador',
            fields=[
                ('id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=15)),
                ('monitor', models.CharField(max_length=15)),
                ('teclado', models.CharField(max_length=15)),
                ('raton', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('marca', models.CharField(max_length=15)),
                ('tamaño', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Raton',
            fields=[
                ('id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('tipoEntrada', models.CharField(max_length=15)),
                ('marca', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Teclado',
            fields=[
                ('id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('tipoEntrada', models.CharField(max_length=15)),
                ('marca', models.CharField(max_length=15)),
            ],
        ),
    ]
