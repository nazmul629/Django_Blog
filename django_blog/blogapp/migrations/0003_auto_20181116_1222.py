# Generated by Django 2.1.3 on 2018-11-16 12:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_auto_20181116_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='artical',
            name='posted_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='artical',
            name='update_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
