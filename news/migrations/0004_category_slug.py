# Generated by Django 3.0.7 on 2020-06-29 11:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('news', '0003_auto_20200624_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='', max_length=100),
            preserve_default=False,
        ),
    ]