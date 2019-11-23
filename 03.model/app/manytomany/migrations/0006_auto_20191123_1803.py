# Generated by Django 2.2.7 on 2019-11-23 09:03

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('manytomany', '0005_auto_20191123_1758'),
    ]

    operations = [
        migrations.CreateModel(
            name='GitHubRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AlterField(
            model_name='instagrampostlike',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.CreateModel(
            name='GitHubUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('following', models.ManyToManyField(blank=True, through='manytomany.GitHubRelation', to='manytomany.GitHubUser')),
            ],
        ),
        migrations.AddField(
            model_name='githubrelation',
            name='from_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relation_set_from_user', to='manytomany.GitHubUser'),
        ),
        migrations.AddField(
            model_name='githubrelation',
            name='to_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relation_set_to_user', to='manytomany.GitHubUser'),
        ),
    ]
