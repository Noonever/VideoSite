# Generated by Django 4.1.7 on 2023-02-27 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0003_video_created_at_alter_video_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created'),
        ),
    ]