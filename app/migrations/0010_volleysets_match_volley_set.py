# Generated by Django 4.1.7 on 2023-10-04 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_chaveamento_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='VolleySets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_a_points', models.IntegerField(default=0)),
                ('team_b_points', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='match',
            name='volley_set',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.volleysets'),
        ),
    ]
