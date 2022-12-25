# Generated by Django 3.2.3 on 2021-08-12 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_rename_size_vehicle_vehicle_class'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved')], default='Pending', max_length=200, null=True),
        ),
    ]
