# Generated by Django 4.1.2 on 2023-05-01 05:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0010_remove_customerconfig_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="customerconfig",
            name="status",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
