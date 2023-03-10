# Generated by Django 4.1.7 on 2023-02-27 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0002_alter_video_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='created_at',
            field=models.DateTimeField(auto_now=True, verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='video',
            name='file',
            field=models.FileField(null=True, upload_to='final_videos', verbose_name='path'),
        ),
    ]
