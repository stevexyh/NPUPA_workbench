# Generated by Django 3.0.6 on 2020-06-14 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('downloader', '0002_filesource_file_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filesource',
            name='file_body',
            field=models.FileField(default='null', upload_to='downloader/contents/'),
        ),
    ]
