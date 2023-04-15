from django.db import models
from django.contrib.auth.models import User


class PlanDuration(models.Model):
    name = models.CharField(max_length=50, null=False)
    duration = models.IntegerField(default=0)
    dsc = models.CharField(max_length=500, null=True, blank=True)
    status = models.IntegerField(default=0)

    class Meta:
        db_table = "plan_duration"

    def __str__(self):
        return self.name


class Plan(models.Model):
    name = models.CharField(max_length=50, null=False)
    dsc = models.CharField(max_length=500, null=True, blank=True)
    status = models.IntegerField(default=0)

    class Meta:
        db_table = "plan"

    def __str__(self):
        return self.name


class PlanPrice(models.Model):
    plan_name = models.CharField(max_length=50, null=False)
    plan_dure = models.CharField(max_length=50, null=False)
    plan = models.ForeignKey(Plan, on_delete=models.SET_NULL, null=True)
    planDuration = models.ForeignKey(
        PlanDuration, on_delete=models.SET_NULL, null=True
    )
    price = models.IntegerField(default=0)
    priceWithDisc = models.IntegerField(default=0)
    status = models.IntegerField(default=0)

    class Meta:
        db_table = "plan_price"

    def __str__(self):
        return self.plan_name + "---" + self.plan_dure


class Customer(models.Model):
    id = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True
    )
    first_name = models.CharField(max_length=150, null=True)
    last_name = models.CharField(max_length=150, null=True)
    phone = models.CharField(max_length=13, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    avatar = models.ImageField(
        null=True, upload_to="profile_image/", blank=True
    )
    status = models.IntegerField(default=0)
    plan = models.ForeignKey(
        Plan, on_delete=models.SET_NULL, null=True, blank=True
    )
    planDuration = models.ForeignKey(
        PlanDuration, on_delete=models.SET_NULL, null=True, blank=True
    )
    updated = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "customer"

    def __str__(self):
        return self.first_name + " " + self.last_name


# Create your models here.
class Exchange(models.Model):
    name = models.CharField(max_length=50, null=False)
    typ = models.CharField(max_length=50, null=False)
    status = models.IntegerField(default=0)
    dsc = models.CharField(max_length=200, null=False)
    updated = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "exchange"

    def __str__(self):
        return self.name


class ServiceType(models.Model):
    name = models.CharField(max_length=50, null=False)
    status = models.IntegerField(default=0)

    class Meta:
        db_table = "service_type"

    def __str__(self):
        return self.name


class Provider(models.Model):
    name = models.CharField(max_length=50, null=False)
    email = models.EmailField(unique=True, null=True)
    phone = models.CharField(max_length=13, null=True)
    dsc = models.CharField(max_length=200, null=True, blank=True)
    status = models.IntegerField(default=0)
    avatar = models.ImageField(
        null=True, upload_to="profile_image/", blank=True
    )
    channel = models.CharField(max_length=50, null=True)
    updated = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "Provider"

    def __str__(self):
        return self.name


class ProviderPrice(models.Model):
    name = models.CharField(max_length=50, null=False)
    planDuration = models.ForeignKey(
        PlanDuration, on_delete=models.SET_NULL, null=True, blank=True
    )
    status = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    priceWithDisc = models.IntegerField(default=0)
    provider = models.ForeignKey(
        Provider, on_delete=models.SET_NULL, null=True, blank=True
    )

    class Meta:
        db_table = "Provider_price"

    def __str__(self):
        # return self.name + ' '+ str(self.priceWithDisct) + ' ' + str(self.price)
        return self.name


class CustomerConfig(models.Model):
    name = models.CharField(max_length=100, null=True)
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, null=True
    )
    referal_key = models.CharField(max_length=100, null=True, blank=True)
    api_name = models.CharField(max_length=100, null=False)
    api_key = models.CharField(max_length=100, null=False)
    api_secret = models.CharField(max_length=100, null=False)
    api_passphrase = models.CharField(max_length=100, null=False)
    trading_pass = models.CharField(max_length=20, null=True, blank=True)
    provider_id = models.IntegerField(default=0, null=True, blank=True)
    channel_id = models.IntegerField(default=0, null=True, blank=True)
    ex_id = models.IntegerField(default=0, null=True, blank=True)
    amuont = models.IntegerField(default=0, null=True, blank=True)
    close_trade = models.IntegerField(default=0, null=True, blank=True)
    grace_percent = models.IntegerField(default=0, null=True, blank=True)
    trailing_en = models.IntegerField(default=0, null=True, blank=True)
    trailing_tp = models.IntegerField(default=0, null=True, blank=True)
    trailing_stop = models.CharField(max_length=50, null=True, blank=True)
    min_symb_interval = models.IntegerField(default=0, null=True, blank=True)
    blacklist_symb = models.CharField(max_length=100, null=True, blank=True)
    blacklist_pair = models.CharField(max_length=100, null=True, blank=True)
    use_ep_percent = models.IntegerField(default=1, null=True, blank=True)
    ep1_percent = models.IntegerField(default=0, null=True, blank=True)
    ep2_percent = models.IntegerField(default=0, null=True, blank=True)
    ep3_percent = models.IntegerField(default=0, null=True, blank=True)
    ep4_percent = models.IntegerField(default=0, null=True, blank=True)
    use_tp_percent = models.IntegerField(default=0, null=True, blank=True)
    tp1_percent = models.IntegerField(default=0, null=True, blank=True)
    tp2_percent = models.IntegerField(default=0, null=True, blank=True)
    tp3_percent = models.IntegerField(default=0, null=True, blank=True)
    tp4_percent = models.IntegerField(default=0, null=True, blank=True)
    tp5_percent = models.IntegerField(null=True, blank=True)
    tp6_percent = models.IntegerField(null=True, blank=True)
    tp7_percent = models.IntegerField(null=True, blank=True)
    tp8_percent = models.IntegerField(null=True, blank=True)
    tp9_percent = models.IntegerField(null=True, blank=True)
    tp10_percent = models.IntegerField(null=True, blank=True)
    status = models.IntegerField(default=0, null=True, blank=True)
    number_tp = models.IntegerField(default=0, null=True, blank=True)
    updated = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "customer_config"

    def __str__(self):
        return self.name


class Invoice(models.Model):
    trx_id = models.CharField(max_length=250, null=True)
    w_customer = models.CharField(max_length=50, null=True)
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True
    )
    PlanPrice = models.ForeignKey(
        PlanPrice, on_delete=models.SET_NULL, null=True
    )
    total_price = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
    updated = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "invoice"


class Plan_feature(models.Model):
    name = models.CharField(max_length=50, null=False)
    status = models.IntegerField(default=0)
    dsc = models.CharField(max_length=200, null=True, blank=True)
    updated = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(null=True, blank=True)
    plan = models.ForeignKey(Plan, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "plan_feature"

    def __str__(self):
        return self.name
