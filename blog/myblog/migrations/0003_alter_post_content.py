# Generated by Django 4.2.7 on 2023-11-24 18:26

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_post_content_alter_post_description_alter_post_h1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
