# Generated by Django 5.0.2 on 2024-03-02 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_mobiles_delete_pravin'),
    ]

    operations = [
        migrations.CreateModel(
            name='My_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('cell', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=20)),
                ('DOB', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Mobiles',
        ),
    ]
