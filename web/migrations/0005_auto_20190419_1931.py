# Generated by Django 2.1 on 2019-04-19 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20190414_2115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='album',
        ),
        migrations.RemoveField(
            model_name='album',
            name='artist',
        ),
        migrations.RemoveField(
            model_name='album',
            name='cover',
        ),
        migrations.RemoveField(
            model_name='album',
            name='discriotion',
        ),
        migrations.RemoveField(
            model_name='album',
            name='like',
        ),
        migrations.RemoveField(
            model_name='album',
            name='rate',
        ),
        migrations.RemoveField(
            model_name='album',
            name='release_date',
        ),
        migrations.RemoveField(
            model_name='album',
            name='summary',
        ),
        migrations.DeleteModel(
            name='Artist',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
