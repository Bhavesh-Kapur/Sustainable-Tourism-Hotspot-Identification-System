# Generated by Django 4.2.7 on 2024-03-16 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sthis_app', '0007_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='desc',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
