# Generated by Django 3.0.5 on 2020-04-08 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='emp_address',
            field=models.CharField(default='my location default', max_length=120),
        ),
        migrations.AddField(
            model_name='profile',
            name='emp_description',
            field=models.TextField(default='description default text'),
        ),
    ]
