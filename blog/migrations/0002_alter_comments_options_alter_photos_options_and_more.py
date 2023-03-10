# Generated by Django 4.1.5 on 2023-02-14 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'verbose_name_plural': 'Comments'},
        ),
        migrations.AlterModelOptions(
            name='photos',
            options={'verbose_name_plural': 'Photos'},
        ),
        migrations.AlterField(
            model_name='comments',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, verbose_name='URL'),
        ),
    ]
