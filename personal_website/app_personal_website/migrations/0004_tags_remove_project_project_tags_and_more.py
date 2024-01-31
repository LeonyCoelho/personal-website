# Generated by Django 5.0 on 2024-01-22 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_personal_website', '0003_project_at_home_project_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='project',
            name='project_tags',
        ),
        migrations.AddField(
            model_name='project',
            name='project_tags',
            field=models.ManyToManyField(to='app_personal_website.tags'),
        ),
    ]
