# Generated by Django 4.1.2 on 2023-03-28 11:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("first_name", models.CharField(max_length=150, null=True)),
                ("last_name", models.CharField(max_length=150, null=True)),
                (
                    "phone",
                    models.CharField(blank=True, max_length=13, null=True),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, null=True, unique=True
                    ),
                ),
                (
                    "avatar",
                    models.ImageField(
                        blank=True, null=True, upload_to="profile_image/"
                    ),
                ),
                ("status", models.IntegerField(default=0)),
                ("updated", models.DateTimeField(blank=True, null=True)),
                ("created", models.DateTimeField(blank=True, null=True)),
            ],
            options={
                "db_table": "customer",
            },
        ),
        migrations.CreateModel(
            name="Exchange",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("typ", models.CharField(max_length=50)),
                ("status", models.IntegerField(default=0)),
                ("dsc", models.CharField(max_length=200)),
                ("updated", models.DateTimeField(blank=True, null=True)),
                ("created", models.DateTimeField(blank=True, null=True)),
            ],
            options={
                "db_table": "exchange",
            },
        ),
        migrations.CreateModel(
            name="Plan",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                (
                    "dsc",
                    models.CharField(blank=True, max_length=500, null=True),
                ),
                ("status", models.IntegerField(default=0)),
            ],
            options={
                "db_table": "plan",
            },
        ),
        migrations.CreateModel(
            name="PlanDuration",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("duration", models.IntegerField(default=0)),
                (
                    "dsc",
                    models.CharField(blank=True, max_length=500, null=True),
                ),
                ("status", models.IntegerField(default=0)),
            ],
            options={
                "db_table": "plan_duration",
            },
        ),
        migrations.CreateModel(
            name="Provider",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                (
                    "email",
                    models.EmailField(max_length=254, null=True, unique=True),
                ),
                ("phone", models.CharField(max_length=13, null=True)),
                (
                    "dsc",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("status", models.IntegerField(default=0)),
                (
                    "avatar",
                    models.ImageField(
                        blank=True, null=True, upload_to="profile_image/"
                    ),
                ),
                ("channel", models.CharField(max_length=50, null=True)),
                ("updated", models.DateTimeField(blank=True, null=True)),
                ("created", models.DateTimeField(blank=True, null=True)),
            ],
            options={
                "db_table": "Provider",
            },
        ),
        migrations.CreateModel(
            name="ServiceType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("status", models.IntegerField(default=0)),
            ],
            options={
                "db_table": "service_type",
            },
        ),
        migrations.CreateModel(
            name="ProviderPrice",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("status", models.IntegerField(default=0)),
                ("price", models.IntegerField(default=0)),
                ("priceWithDisc", models.IntegerField(default=0)),
                (
                    "planDuration",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="base.planduration",
                    ),
                ),
                (
                    "provider",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="base.provider",
                    ),
                ),
            ],
            options={
                "db_table": "Provider_price",
            },
        ),
        migrations.CreateModel(
            name="PlanPrice",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("plan_name", models.CharField(max_length=50)),
                ("plan_dure", models.CharField(max_length=50)),
                ("price", models.IntegerField(default=0)),
                ("priceWithDisc", models.IntegerField(default=0)),
                ("status", models.IntegerField(default=0)),
                (
                    "plan",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="base.plan",
                    ),
                ),
                (
                    "planDuration",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="base.planduration",
                    ),
                ),
            ],
            options={
                "db_table": "plan_price",
            },
        ),
        migrations.CreateModel(
            name="Plan_feature",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("status", models.IntegerField(default=0)),
                (
                    "dsc",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("updated", models.DateTimeField(blank=True, null=True)),
                ("created", models.DateTimeField(blank=True, null=True)),
                (
                    "plan",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="base.plan",
                    ),
                ),
            ],
            options={
                "db_table": "plan_feature",
            },
        ),
        migrations.CreateModel(
            name="Invoice",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("trx_id", models.CharField(max_length=250, null=True)),
                ("w_customer", models.CharField(max_length=50, null=True)),
                ("total_price", models.IntegerField(default=0)),
                ("status", models.IntegerField(default=0)),
                ("updated", models.DateTimeField(blank=True, null=True)),
                ("created", models.DateTimeField(blank=True, null=True)),
                (
                    "PlanPrice",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="base.planprice",
                    ),
                ),
                (
                    "customer",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="base.customer",
                    ),
                ),
            ],
            options={
                "db_table": "invoice",
            },
        ),
        migrations.CreateModel(
            name="CustomerConfig",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, null=True)),
                (
                    "referal_key",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("api_name", models.CharField(max_length=100)),
                ("api_key", models.CharField(max_length=100)),
                ("api_secret", models.CharField(max_length=100)),
                ("api_passphrase", models.CharField(max_length=100)),
                (
                    "trading_pass",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                ("provider_id", models.IntegerField(default=0)),
                ("channel_id", models.IntegerField(default=0)),
                ("ex_id", models.IntegerField(default=0)),
                ("amuont", models.IntegerField(default=0)),
                ("close_trade", models.IntegerField(default=0, null=True)),
                ("grace_percent", models.IntegerField(default=0, null=True)),
                ("trailing_en", models.IntegerField(default=0, null=True)),
                ("trailing_tp", models.IntegerField(default=0, null=True)),
                ("trailing_stop", models.CharField(max_length=50, null=True)),
                (
                    "min_symb_interval",
                    models.IntegerField(default=0, null=True),
                ),
                (
                    "blacklist_symb",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "blacklist_pair",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("use_ep_percent", models.IntegerField(default=1, null=True)),
                ("ep1_percent", models.FloatField(blank=True, null=True)),
                ("ep2_percent", models.FloatField(blank=True, null=True)),
                ("ep3_percent", models.FloatField(blank=True, null=True)),
                ("ep4_percent", models.FloatField(blank=True, null=True)),
                (
                    "use_tp_percent",
                    models.IntegerField(blank=True, null=True),
                ),
                ("tp1_percent", models.IntegerField(blank=True, null=True)),
                ("tp2_percent", models.IntegerField(blank=True, null=True)),
                ("tp3_percent", models.IntegerField(blank=True, null=True)),
                ("tp4_percent", models.IntegerField(blank=True, null=True)),
                ("tp5_percent", models.IntegerField(blank=True, null=True)),
                ("tp6_percent", models.IntegerField(blank=True, null=True)),
                ("tp7_percent", models.IntegerField(blank=True, null=True)),
                ("tp8_percent", models.IntegerField(blank=True, null=True)),
                ("tp9_percent", models.IntegerField(blank=True, null=True)),
                ("tp10_percent", models.IntegerField(blank=True, null=True)),
                (
                    "status",
                    models.IntegerField(blank=True, default=0, null=True),
                ),
                ("number_tp", models.IntegerField(default=0, null=True)),
                ("updated", models.DateTimeField(blank=True, null=True)),
                ("created", models.DateTimeField(blank=True, null=True)),
                (
                    "customer",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="base.customer",
                    ),
                ),
            ],
            options={
                "db_table": "customer_config",
            },
        ),
        migrations.AddField(
            model_name="customer",
            name="plan",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="base.plan",
            ),
        ),
        migrations.AddField(
            model_name="customer",
            name="planDuration",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="base.planduration",
            ),
        ),
    ]
