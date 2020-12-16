# Generated by Django 3.1.2 on 2020-11-29 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0006_auto_20201129_2301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='store_id',
        ),
        migrations.AddField(
            model_name='product',
            name='store_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='stores.store'),
            preserve_default=False,
        ),
    ]
