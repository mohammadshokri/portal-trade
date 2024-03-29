# Generated by Django 4.1.2 on 2023-04-16 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0006_alter_customerconfig_ep1_percent_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customerconfig",
            name="provider_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="base.provider",
            ),
        ),
    ]
