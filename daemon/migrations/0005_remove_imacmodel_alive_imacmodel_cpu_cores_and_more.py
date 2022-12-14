# Generated by Django 4.1.2 on 2022-11-04 20:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("daemon", "0004_imacmodel_alive_imacmodel_last_seen"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="imacmodel",
            name="alive",
        ),
        migrations.AddField(
            model_name="imacmodel",
            name="cpu_cores",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="imacmodel",
            name="macos_build_version",
            field=models.CharField(default="", max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="imacmodel",
            name="macos_version",
            field=models.CharField(default="", max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="imacmodel",
            name="memory",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="imacmodel",
            name="serial_number",
            field=models.CharField(default="", max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="imacmodel",
            name="status",
            field=models.CharField(
                choices=[
                    ("Unavailable", "Unavailable"),
                    ("Available", "Available"),
                    ("In Use", "In Use"),
                ],
                default="Unavailable",
                max_length=255,
            ),
        ),
        migrations.AddField(
            model_name="imacmodel",
            name="storage_capacity",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
