# Generated by Django 4.1.7 on 2024-05-11 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=20, unique=True)),
                ('description', models.TextField(max_length=300)),
            ],
            options={
                'db_table': 'Services',
            },
        ),
    ]
