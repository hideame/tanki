# Generated by Django 2.2.4 on 2019-09-29 06:09

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('skill', '0011_auto_20190929_0540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='image',
            field=stdimage.models.StdImageField(blank=True, upload_to='photo'),
        ),
    ]
