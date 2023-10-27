# Generated by Django 4.2.6 on 2023-10-27 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('date_of_registration', models.DateField()),
                ('role', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=255)),
                ('date_of_creation', models.DateField()),
                ('status', models.BooleanField()),
                ('priority', models.CharField(max_length=255)),
                ('executor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
    ]