# Generated by Django 2.2.7 on 2019-11-23 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manytomany', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='instagrampost',
            name='tags',
            field=models.ManyToManyField(blank=True, to='manytomany.HashTag'),
        ),
    ]
