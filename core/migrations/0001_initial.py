# Generated by Django 3.0 on 2019-12-08 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('valor', models.IntegerField()),
                ('descripcion', models.CharField(max_length=300)),
                ('estado', models.CharField(max_length=20)),
                ('stock', models.IntegerField()),
            ],
        ),
    ]
