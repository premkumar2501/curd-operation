# Generated by Django 5.0.2 on 2024-03-19 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0009_demo_delete_place_delete_values'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=25)),
            ],
        ),
        migrations.DeleteModel(
            name='Demo',
        ),
    ]
