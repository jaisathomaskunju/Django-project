# Generated by Django 2.2.4 on 2019-10-28 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('textileapp', '0014_coupon'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coupon',
            old_name='price',
            new_name='cprice',
        ),
    ]
