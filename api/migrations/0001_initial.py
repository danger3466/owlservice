# Generated by Django 3.0.3 on 2020-03-04 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.CharField(max_length=254)),
                ('date_create', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'comments',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.AutoField(db_column='model_id', primary_key=True, serialize=False)),
                ('model_name', models.CharField(max_length=64)),
                ('model_photo', models.CharField(blank=True, max_length=255, null=True)),
                ('model_url', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'db_table': 'models',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(db_column='status_id', primary_key=True, serialize=False)),
                ('status_name', models.CharField(max_length=24)),
                ('status_style', models.CharField(max_length=8)),
                ('status_icon', models.CharField(max_length=16)),
            ],
            options={
                'db_table': 'status',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(db_column='ticket_id', primary_key=True, serialize=False)),
                ('client_name', models.CharField(max_length=48)),
                ('client_phone', models.CharField(blank=True, max_length=18, null=True)),
                ('imei', models.BigIntegerField(blank=True, null=True)),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tickets',
                'managed': False,
            },
        ),
    ]
