# Generated by Django 3.2.6 on 2021-08-24 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoas',
            name='cpf',
            field=models.IntegerField(default=0, max_length=10),
        ),
    ]
