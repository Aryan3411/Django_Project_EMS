# Generated by Django 4.2.6 on 2023-10-22 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('joinDate', models.DateField()),
                ('birthDate', models.DateField()),
                ('email', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=15)),
                ('salary', models.CharField(max_length=50)),
            ],
        ),
    ]