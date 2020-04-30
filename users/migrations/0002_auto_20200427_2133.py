# Generated by Django 2.2.12 on 2020-04-27 20:33

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default='user_logo.png', null=True, upload_to=users.models.imageUploadLocation),
        ),
    ]
