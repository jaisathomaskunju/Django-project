# Generated by Django 2.2.4 on 2019-10-12 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogapps', '0023_blogs'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='blog',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='blogapps.Blogs'),
        ),
    ]
