# Generated by Django 4.0.1 on 2022-06-08 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0002_song_singer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singer',
            name='song',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='singer', to='practice.song'),
        ),
    ]
