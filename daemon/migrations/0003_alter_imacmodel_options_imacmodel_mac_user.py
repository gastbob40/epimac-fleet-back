# Generated by Django 4.1.2 on 2022-10-28 20:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("daemon", "0002_rename_imac_imacmodel"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="imacmodel",
            options={"verbose_name": "IMac", "verbose_name_plural": "IMacs"},
        ),
        migrations.AddField(
            model_name="imacmodel",
            name="mac_user",
            field=models.CharField(default="", max_length=255),
            preserve_default=False,
        ),
    ]
