# Generated by Django 4.1.2 on 2023-05-02 09:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0012_customer_email"),
    ]

    operations = [
        migrations.AddField(
            model_name="customer",
            name="password",
            field=models.CharField(max_length=150, null=True),
        ),
    ]