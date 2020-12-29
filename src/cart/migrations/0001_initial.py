# Generated by Django 3.1.4 on 2020-12-29 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full', models.BooleanField(default=False)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=10000)),
            ],
        ),
    ]