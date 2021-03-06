# Generated by Django 3.2.10 on 2021-12-17 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts2', '0002_auto_20210925_0726'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='click_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='first_category',
            field=models.CharField(default='ca1', max_length=5),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_category',
            field=models.CharField(default='ca1', max_length=5),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_modified',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
