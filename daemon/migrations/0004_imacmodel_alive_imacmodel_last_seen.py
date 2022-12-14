# Generated by Django 4.1.2 on 2022-10-28 20:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("daemon", "0003_alter_imacmodel_options_imacmodel_mac_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="imacmodel",
            name="alive",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="imacmodel",
            name="last_seen",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
