# Generated by Django 4.2.7 on 2024-03-16 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sthis_app', '0004_rename_full_name_profile_first_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='P',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]