# Generated by Django 3.2.5 on 2022-01-30 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0005_alter_dealer_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_no', models.CharField(max_length=10)),
                ('color', models.CharField(max_length=10)),
            ],
        ),
    ]
