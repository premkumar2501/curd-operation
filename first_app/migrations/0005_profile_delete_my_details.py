# Generated by Django 5.0.2 on 2024-03-03 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0004_rename_cell_my_details_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Mother', models.CharField(max_length=20)),
                ('Father', models.CharField(max_length=20)),
                ('Phone', models.IntegerField(max_length=20)),
                ('Email', models.CharField(max_length=20)),
                ('Date_of_birth', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='My_details',
        ),
    ]