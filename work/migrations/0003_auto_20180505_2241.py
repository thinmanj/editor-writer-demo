# Generated by Django 2.0.5 on 2018-05-05 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0002_auto_20180505_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='description',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='article',
            name='summary',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='article',
            name='document',
            field=models.URLField(default='', max_length=1000),
        ),
    ]
