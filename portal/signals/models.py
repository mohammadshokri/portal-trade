from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from base.models import Customer, Provider, Exchange


class Signal(models.Model):
    status = models.IntegerField(default=0, null=True, blank=True)

    # typ = models.IntegerField(default=0, choices=((1, 'Spot'), (2, 'Future')))
    typ = models.IntegerField(default=0)
    side = models.IntegerField(default=0)
    number_ep = models.IntegerField(default=0, null=True, blank=True)
    ep1 = models.FloatField(default=0, null=True, blank=True)
    ep2 = models.FloatField(default=0, null=True, blank=True)
    ep3 = models.FloatField(default=0, null=True, blank=True)
    ep4 = models.FloatField(default=0, null=True, blank=True)
    number_tp = models.IntegerField(default=0, null=True, blank=True)
    sl_number = models.FloatField(default=0, null=True, blank=True)
    # be = models.CharField(max_length=40, null=True,blank=True)
    Llv = models.FloatField(default=0, null=True, blank=True)
    lv_typ = models.FloatField(default=0, null=True, blank=True)
    en_user = models.IntegerField(default=0, null=True, blank=True)
    job_name = models.CharField(max_length=20, null=True, blank=True)
    updated = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(null=True, blank=True)
    provider = models.ForeignKey(
        Provider, on_delete=models.SET_NULL, null=True, blank=True
    )
    exchange = models.ForeignKey(
        Exchange, on_delete=models.SET_NULL, null=True
    )

    class Meta:
        db_table = "signal"

    def __str__(self):
        return self.typ


class SignalDt(models.Model):
    signal = models.ForeignKey(Signal, on_delete=models.SET_NULL, null=True)
    tp = models.FloatField(default=0)
    tp_percent = models.PositiveIntegerField(default=0)
    updated = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "signal_dt"

    def __str__(self):
        return f"Id: {self.pk }, {self.signal} for SignalId: {self.signal.pk}"


class SignalOrder(models.Model):
    client_id = models.CharField(max_length=200, null=False)
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True
    )
    exchange = models.ForeignKey(
        Exchange, on_delete=models.SET_NULL, null=True
    )
    api_key = models.CharField(max_length=100, null=False)
    api_secret = models.CharField(max_length=100, null=False)
    api_passphrase = models.CharField(max_length=100, null=False)
    sig_typ = models.CharField(max_length=100, null=True)
    side = models.IntegerField(default=0, null=True)
    symb = models.CharField(max_length=20, null=True)
    amount_db = models.FloatField(default=0)
    pr_sym_db = models.FloatField(default=0)
    pr_sym_set = models.FloatField(default=0)
    ep = models.FloatField(default=0)
    ep_opt = models.FloatField(default=0)
    sl = models.FloatField(default=0, null=False, blank=True)
    trail_en = models.IntegerField(default=0, null=True, blank=True)
    trail_tp = models.IntegerField(default=0, null=True, blank=True)
    trail_sl = models.IntegerField(default=0, null=True, blank=True)
    status = models.IntegerField(default=0)
    number = models.IntegerField(default=1)
    job = models.CharField(max_length=200, null=False)
    bin_order_id = models.CharField(max_length=20, null=False)
    signal = models.ForeignKey(Signal, on_delete=models.SET_NULL, null=True)
    amount_set = models.IntegerField(default=0, null=False, blank=True)
    ep_pre = models.IntegerField(default=0, null=True, blank=True)
    updated = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "signal_order"


class SisgnalOrderDt(models.Model):
    order = models.ForeignKey(
        SignalOrder, on_delete=models.SET_NULL, null=True
    )
    client_id = models.CharField(max_length=100, null=False)
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True
    )
    symb = models.CharField(max_length=20, null=False)
    tp = models.FloatField(default=0)
    tp_am = models.FloatField(default=0)
    status = models.IntegerField(default=1)
    bin_order_id = models.CharField(max_length=20, null=False)
    signal = models.ForeignKey(Signal, on_delete=models.SET_NULL, null=True)
    updated = models.DateTimeField(null=True)
    created = models.DateTimeField(null=True)

    class Meta:
        db_table = "signal_order_dt"


class SigOrderSl(models.Model):
    order_id = models.IntegerField
    client_id = models.CharField(max_length=100, null=False)
    user_id = models.IntegerField(default=0)
    symb = models.CharField(max_length=20, null=False)
    sl = models.FloatField(default=0)
    status = models.IntegerField(default=0)
    number = models.IntegerField(default=1)
    bin_order_id = models.CharField(max_length=20, null=False)
    signal = models.ForeignKey(
        SignalOrder, on_delete=models.SET_NULL, null=True
    )
    amount_set = models.FloatField(default=0)
    updated = models.DateTimeField(null=True)
    created = models.DateTimeField(null=True)

    class Meta:
        db_table = "signal_order_sl"


class MarketPrice(models.Model):
    name = models.CharField(max_length=30, null=False)
    prc = models.FloatField(default=0)
    pre_prc = models.FloatField(default=0)
    side = models.IntegerField(default=0)
    updated = models.DateTimeField(null=True)
    created = models.DateTimeField(null=True)

    class Meta:
        db_table = "market_price"

    def __str__(self):
        return self.name
