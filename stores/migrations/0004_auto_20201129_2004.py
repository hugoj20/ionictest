# Generated by Django 3.1.2 on 2020-11-29 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0003_auto_20201129_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='logo_url',
            field=models.CharField(max_length=200),
        ),
    ]
