# Generated by Django 4.1.7 on 2023-10-03 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_chaveamento'),
    ]

    operations = [
        migrations.AddField(
            model_name='chaveamento',
            name='title',
            field=models.CharField(default='untitled', max_length=200),
        ),
    ]
