# Generated by Django 3.1.4 on 2020-12-31 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_remove_photo_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
