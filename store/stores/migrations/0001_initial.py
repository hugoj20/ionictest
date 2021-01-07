# Generated by Django 3.1.2 on 2021-01-07 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_lastupdated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=100)),
                ('url_photos', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('stock', models.PositiveIntegerField()),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('suspended', 'Suspended'), ('deleted', 'deleted')], default='active', max_length=20)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_lastupdated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('date_created',),
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('store_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('keywords', models.CharField(max_length=200)),
                ('logo_url', models.CharField(max_length=200)),
                ('banner_url', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('facebook', models.CharField(max_length=200)),
                ('instagram', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('suspended', 'Suspended'), ('deleted', 'deleted')], default='active', max_length=20)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_lastupdated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
