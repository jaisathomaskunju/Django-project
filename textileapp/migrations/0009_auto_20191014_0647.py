# Generated by Django 2.2.4 on 2019-10-14 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('textileapp', '0008_auto_20191014_0625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='title',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='textileapp.Textile'),
        ),
    ]