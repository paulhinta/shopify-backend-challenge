# Generated by Django 3.1.4 on 2021-01-11 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_auto_20210104_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='available',
            field=models.BooleanField(default=True, verbose_name='Leave this box checked to make your Photo available for purchase. You can always change this later.'),
        ),
    ]
