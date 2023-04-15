from django import forms
from .models import Ticket, TicketDetail, TicketSubject
from django.forms import ModelForm
from django.forms import inlineformset_factory


class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ["priority", "ticketSubject"]


class TicketSubjectForm(ModelForm):
    class Meta:
        model = TicketSubject
        fields = "__all__"


# class TicketForm(forms.ModelForm):
#     class Meta:
#         model = Ticket
#
#         widgets = {
#             'description': forms.Textarea(),
#             'creator': forms.HiddenInput(),
#         }
#
#         fields = [
#             'ticketType',
#             'subject',
#             'project',
#             'description',
#             'priority',
#             'status',
#             'creator',
#             'owner',
#         ]
#
#         # help_texts = {
#         #     'subject': 'Group to which this message belongs to',
#         # }
#
#         # error_messages={
#         #     'required': 'Please enter your name'
#         # }


class TicketDetailForm(ModelForm):
    class Meta:
        model = TicketDetail
        fields = ["req"]
