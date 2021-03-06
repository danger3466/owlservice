# Generated by Django 3.0.3 on 2020-03-03 08:59

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(db_column='user_id', primary_key=True, serialize=False)),
                ('user_id_parent_id', models.PositiveIntegerField(blank=True, null=True)),
                ('user_fullname', models.CharField(blank=True, max_length=128, null=True)),
                ('user_company', models.CharField(blank=True, max_length=48, null=True)),
                ('user_company_address', models.CharField(blank=True, max_length=128, null=True)),
                ('user_company_tel', models.CharField(blank=True, max_length=32, null=True)),
                ('user_company_logo', models.CharField(blank=True, max_length=256, null=True)),
                ('username', models.CharField(db_column='user_name', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()])),
                ('email', models.EmailField(blank=True, db_column='user_email', max_length=254)),
                ('password', models.CharField(blank=True, db_column='user_password', max_length=32, null=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
