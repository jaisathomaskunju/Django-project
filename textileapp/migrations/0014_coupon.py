# Generated by Django 2.2.4 on 2019-10-28 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textileapp', '0013_auto_20191025_0706'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default=None, max_length=10)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
    ]