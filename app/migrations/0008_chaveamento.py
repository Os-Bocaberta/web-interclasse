# Generated by Django 4.1.7 on 2023-10-03 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_penalties_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chaveamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='chaveamento/')),
            ],
        ),
    ]
