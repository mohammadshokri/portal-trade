from django.forms import ModelForm
from . import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import inlineformset_factory


TYPE_CHOICE = [
    (1, "Spot"),
    (2, "Future"),
]
SIDE_CHOICE = [
    (1, "Buy"),
    (2, "Sell"),
]
STATUS_CHOICE = [
    (1, "Active"),
    (2, "Inactive"),
]

NUMBER_TP_CHOICE = [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
    (9, 9),
    (10, 10),
]


################Singal Create Forms
###################################
class SignalForm(forms.ModelForm):
    # typ =  forms.ChoiceField(choices = TYPE_CHOICE, widget=forms.Select(attrs={'onchange':'fnc_type_change();'}), initial=1)
    # number_tp =forms.ChoiceField(choices = NUMBER_TP_CHOICE, initial=1, widget=forms.Select(attrs={'class': 'form-control'}))
    # exchange = forms.ModelChoiceField(queryset=models.Exchange.objects.all() , initial=1,
    #                                   widget=forms.Select(attrs={'class': 'form-control'}))
    # side = forms.ChoiceField(choices = SIDE_CHOICE, widget=forms.Select(attrs={'class': 'form-control'}))
    # status = forms.ChoiceField(choices = STATUS_CHOICE, widget=forms.Select(attrs={'class': 'form-control'}))
    # ep1 = forms.FloatField(min_value=0,   )
    # ep2 = forms.FloatField(min_value=0)
    # ep3 = forms.FloatField(min_value=0)
    # ep4 = forms.FloatField(min_value=0)
    # sl_number = forms.FloatField(min_value=0)
    # llv = forms.FloatField(min_value=0,help_text="Enter a Positive Number" )
    #
    # def clean_ep2(self):
    #     ep2 = self.cleaned_data['ep2']
    #     if ep2 == None or ep2 > 0:
    #         return ep2
    #     else:
    #         raise forms.ValidationError('Ep2 cannot be Null or Negative number')
    class Meta:
        model = models.Signal
        fields = "__all__"
        # = forms.ChoiceField(choices=TYPE_CHOICE)


class SignalDetailForm(forms.ModelForm):
    tp = forms.FloatField(min_value=0)

    class Meta:
        model = models.SignalDt
        fields = "__all__"


SignalDetailInlineFormset = inlineformset_factory(
    models.Signal,
    models.SignalDt,
    form=SignalDetailForm,
    extra=10,
    can_delete=False,
    validate_min=True,
    min_num=0,
    # max_num=10,
    # fk_name=None,
    # fields=None, exclude=None, can_order=False,
    # max_num=None, formfield_callback=None,
    # widgets=None, validate_max=False, localized_fields=None,
    # labels=None, help_texts=None, error_messages=None,
    #  field_classes=None
)
