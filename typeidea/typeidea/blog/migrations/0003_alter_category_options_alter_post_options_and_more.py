# Generated by Django 4.1.7 on 2023-02-21 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_auto_20220329_1417"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name": "2-分类", "verbose_name_plural": "2-分类"},
        ),
        migrations.AlterModelOptions(
            name="post",
            options={
                "ordering": ["-id"],
                "verbose_name": "1-文章",
                "verbose_name_plural": "1-文章",
            },
        ),
        migrations.AlterModelOptions(
            name="tag",
            options={"verbose_name": "3-标签", "verbose_name_plural": "3-标签"},
        ),
        migrations.AddField(
            model_name="post",
            name="pv",
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name="post",
            name="uv",
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name="category",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="tag",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
