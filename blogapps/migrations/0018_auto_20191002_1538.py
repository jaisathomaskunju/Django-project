# Generated by Django 2.2.4 on 2019-10-02 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapps', '0017_blogs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='image',
            field=models.ImageField(blank=True, default='pics/author.jpg', upload_to='pics/'),
        ),
    ]
