# Generated by Django 4.1.7 on 2023-10-02 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_match_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='penalties',
            name='type',
            field=models.IntegerField(choices=[(None, 'Vazio'), (0, 'Falta'), (1, 'Cartão Amarelo'), (2, 'Cartão Vermelho'), (3, 'Bloqueio'), (4, 'Erro')]),
        ),
    ]
