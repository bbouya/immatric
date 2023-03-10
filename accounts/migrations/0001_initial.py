# Generated by Django 3.2.3 on 2022-09-23 22:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50, null=True)),
                ('gender', models.CharField(blank=True, max_length=25)),
                ('birth_date', models.DateField(null=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone', phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31)),
                ('apt_unit', models.IntegerField(blank=True, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Parkingspace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_space', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_plate', models.CharField(blank=True, max_length=50, null=True)),
                ('make', models.CharField(blank=True, max_length=50, null=True)),
                ('model', models.CharField(blank=True, max_length=100, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('color', models.CharField(blank=True, max_length=50, null=True)),
                ('vehicle_class', models.CharField(blank=True, max_length=50, null=True)),
                ('parked', models.BooleanField(blank=True, default=False, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved')], default='Pending', max_length=200, null=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.customer')),
            ],
        ),
    ]
