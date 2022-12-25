# Generated by Django 3.2.3 on 2021-08-13 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_vehicle_parked'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parkingspace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField(blank=True, null=True)),
                ('occupied', models.IntegerField(blank=True, null=True)),
                ('available', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]