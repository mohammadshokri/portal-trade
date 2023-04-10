from django.forms import ModelForm
from . import models
from tickets.models import Ticket, TicketDetail

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import inlineformset_factory


class UserForm(UserCreationForm):
    # phone = forms.CharField()
    class Meta:
        model = User
        fields = ['username', 'password1','password2','first_name', 'last_name', 'email']


class PlanDurationForm(forms.Form):
    planDuration = forms.ModelChoiceField(queryset=models.PlanDuration.objects.filter(status='1'), initial=0, to_field_name="id")
    # , initial=0, to_field_name="id" , widget=forms.Select(attrs={'onchange': 'submit();'}))

class ServiceTypeForm(forms.Form):
    serviceName = forms.ModelChoiceField(queryset=models.ServiceType.objects.filter(status='1'), initial=0, to_field_name="id")

class ProviderPriceForm(forms.Form):
    providerName = forms.ModelChoiceField(queryset=models.Provider.objects.filter(status='1'), initial=0, to_field_name="id")

class PlanForm(forms.Form):
    planName = forms.ModelChoiceField(queryset=models.Plan.objects.filter(status='1'), initial=0, to_field_name="id")


class CustomerForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    class Meta:
        model = models.Customer
        fields = '__all__'

class TrxForm(ModelForm):
    class Meta:
        model = models.Invoice
        fields = '__all__'


TYPE_CHOICE = [
    (1, 'Spot'),
    (2, 'Future'),
]
SIDE_CHOICE = [
    (1, 'Buy'),
    (2, 'Sell'),
]
STATUS_CHOICE = [
    (1, 'Active'),
    (2, 'Inactive'),
]

NUMBER_TP_CHOICE =[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10)]

class CustomerConfigForm(ModelForm):
    class Meta:
        model = models.CustomerConfig
        fields = '__all__'

