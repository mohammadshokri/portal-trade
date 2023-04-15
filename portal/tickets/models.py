from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from base.models import Customer


class TicketSubject(models.Model):  # 1 to many
    name = models.CharField(max_length=50, null=False)
    status = models.IntegerField(default=1, null=False, blank=True)
    dsc = models.CharField(max_length=300, null=True, blank=True)
    updated = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "ticket_subject"

    def __str__(self):
        return self.name


class Ticket(models.Model):
    PRIORITY_CHOICES = (
        ("Low", "Low"),
        ("Medium", "Medium"),
        ("High", "High"),
        ("Critical", "Critical"),
    )
    STATUS_CHOICES = (
        ("Open", "Open"),
        ("Waiting On Submitter", "Waiting On Submitter"),
        ("In Progress", "In Progress"),
        ("Waiting On Support", "Waiting On Support"),
        ("Resolved", "Resolved"),
    )
    ticketSubject = models.ForeignKey(TicketSubject, on_delete=models.CASCADE)
    priority = models.CharField(
        max_length=10, choices=PRIORITY_CHOICES, blank=True
    )
    status = models.CharField(
        max_length=40, choices=STATUS_CHOICES, blank=True
    )
    user = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    updated = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(null=True, blank=True)

    def how_many_days_old(self):
        delta = timezone.now() - self.created
        return delta.days

    # def shortened_subject_str(self):
    #     return self.subject[0:20]

    # def get_absolute_url(self):
    #     return reverse('tickets:ticket_detail', args=[str(self.id)])

    def __str__(self):
        return self.ticketSubject.name + "-" + str(self.id)

    class Meta:
        db_table = "ticket"


class TicketDetail(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.SET_NULL, null=True)
    status = models.IntegerField(default=1)
    req = models.CharField(max_length=500, null=True, blank=True)
    resp = models.CharField(max_length=1000, null=True, blank=True)
    updated = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "ticket_dt"
