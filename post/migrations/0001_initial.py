# Generated by Django 2.2.12 on 2020-04-29 15:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import post.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(max_length=2000, verbose_name='Add Comment')),
                ('date_commented', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('post_image', models.ImageField(default='post.png', upload_to=post.models.imageUploadLocation)),
                ('category', models.CharField(choices=[('python', 'python'), ('php', 'php'), ('java', 'java'), ('c/c++', 'c/c++'), ('web', 'web'), ('gui', 'gui'), ('AI', 'AI'), ('DSA', 'DSA'), ('other', 'other')], max_length=50)),
                ('body', models.TextField(help_text='You can include html tags!')),
                ('url', models.URLField(blank=True)),
                ('slug', models.SlugField(unique=True)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(blank=True, related_name='Likes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CommentReplie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply', models.TextField(blank=True, max_length=1000, verbose_name='Reply')),
                ('Comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.Comment')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.Post')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.Post'),
        ),
    ]
