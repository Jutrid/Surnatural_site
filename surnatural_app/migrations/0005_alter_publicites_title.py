# Generated by Django 4.1.7 on 2024-05-14 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surnatural_app', '0004_publicites'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicites',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
