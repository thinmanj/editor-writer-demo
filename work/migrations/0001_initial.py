# Generated by Django 2.0.5 on 2018-05-05 21:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.URLField(max_length=1000)),
                ('status', models.IntegerField(choices=[(1, 'Open'), (2, 'Assigned'), (3, 'For Review'), (4, 'Approved')], default=1)),
                ('editor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='editors', to=settings.AUTH_USER_MODEL)),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wirters', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
