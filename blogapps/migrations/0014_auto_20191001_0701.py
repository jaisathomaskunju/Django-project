# Generated by Django 2.2.4 on 2019-10-01 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapps', '0013_auto_20191001_0700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='image',
            field=models.ImageField(default='author.jpg', upload_to='pics/'),
        ),
    ]
