# Generated by Django 4.2.7 on 2024-01-03 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('Sname', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('Slocation', models.CharField(max_length=100)),
                ('Sprincipal', models.CharField(max_length=100)),
            ],
        ),
    ]
