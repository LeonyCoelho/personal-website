# Generated by Django 4.2.7 on 2023-11-17 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=40)),
                ('project_type', models.CharField(max_length=30)),
                ('project_images', models.CharField(max_length=500)),
                ('project_description', models.CharField(max_length=2000)),
            ],
        ),
    ]
