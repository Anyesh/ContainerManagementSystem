# Generated by Django 2.1.3 on 2018-11-28 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20181128_1514'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='departed',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='received',
        ),
        migrations.AddField(
            model_name='container',
            name='departed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='container',
            name='received',
            field=models.BooleanField(default=False),
        ),
    ]
