# Generated by Django 2.2.4 on 2019-10-02 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapps', '0018_auto_20191002_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to='media/pics/'),
        ),
    ]