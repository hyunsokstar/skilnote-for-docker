# Generated by Django 3.2.7 on 2021-09-24 21:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wm', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SkilBlogTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('reputation', models.IntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SkilBlogContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('filename', models.CharField(blank=True, max_length=120)),
                ('content1', models.CharField(blank=True, max_length=180)),
                ('content2', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, upload_to='wm/%y%m%d')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('sbt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skilblog.skilblogtitle')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wm.type')),
            ],
        ),
        migrations.CreateModel(
            name='LikeForSkilBlogTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('sbt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skilblog.skilblogtitle')),
            ],
        ),
        migrations.CreateModel(
            name='CommentForSkilBlogTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('sbt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='skilblog.skilblogtitle')),
            ],
        ),
    ]
