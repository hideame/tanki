# Generated by Django 2.2.4 on 2019-09-24 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skill', '0009_delete_favorite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='favorite_num',
        ),
    ]
