# Generated by Django 3.1 on 2023-03-03 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_auto_20200902_0116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='listing'),
        ),
    ]
