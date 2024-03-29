# Generated by Django 2.2.4 on 2019-10-25 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textileapp', '0012_checkout'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='email',
            field=models.EmailField(default=None, max_length=254),
        ),
        migrations.AddField(
            model_name='checkout',
            name='firstname',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AddField(
            model_name='checkout',
            name='lastname',
            field=models.CharField(default=None, max_length=20),
        ),
    ]
