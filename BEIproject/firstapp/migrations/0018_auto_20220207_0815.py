# Generated by Django 3.2.5 on 2022-02-07 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0017_auto_20220207_0808'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='citizenship_back',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='citizenship_front',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='driving_license',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
    ]
