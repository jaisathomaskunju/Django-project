# Generated by Django 2.2.4 on 2019-10-28 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textileapp', '0015_auto_20191028_0809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='phone',
            field=models.PositiveIntegerField(default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='postcode',
            field=models.PositiveIntegerField(default=None, max_length=6),
        ),
    ]