# Generated by Django 4.1.7 on 2023-03-10 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0005_post_content_html"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="post",
            options={"verbose_name": "1-文章", "verbose_name_plural": "1-文章"},
        ),
    ]