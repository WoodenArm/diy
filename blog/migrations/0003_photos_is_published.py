# Generated by Django 4.1.5 on 2023-02-21 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_comments_options_alter_photos_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='photos',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
    ]
