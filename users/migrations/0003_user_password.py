# Generated by Django 3.1.2 on 2020-11-22 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20201116_0059'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='aaa', max_length=255),
            preserve_default=False,
        ),
    ]
