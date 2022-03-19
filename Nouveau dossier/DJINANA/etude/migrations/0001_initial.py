# Generated by Django 3.1.1 on 2022-03-19 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Probleme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_prenom', models.CharField(max_length=255)),
                ('localisation', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Probleme',
                'verbose_name_plural': 'Problemes',
            },
        ),
    ]
