# Generated by Django 3.0 on 2023-08-22 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=20)),
                ('branch', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=20)),
            ],
        ),
    ]
