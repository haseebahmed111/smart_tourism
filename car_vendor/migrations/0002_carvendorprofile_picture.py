# Generated by Django 4.0.1 on 2022-04-14 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_vendor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carvendorprofile',
            name='picture',
            field=models.ImageField(blank=True, upload_to='car_vendor_images/'),
        ),
    ]
