# Generated by Django 2.2.4 on 2019-09-04 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skill', '0003_photo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Photo',
        ),
        migrations.AddField(
            model_name='service',
            name='image',
            field=models.ImageField(null=True, upload_to='photo'),
        ),
    ]
