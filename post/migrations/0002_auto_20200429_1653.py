# Generated by Django 2.2.12 on 2020-04-29 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commentreplie',
            old_name='Comment',
            new_name='comment',
        ),
    ]
