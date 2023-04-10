from django.shortcuts import render, redirect
from django.http import HttpResponse , HttpResponseRedirect
from . import models
from tickets.models import TicketDetail
from .form import CustomerForm, CustomerConfigForm, ModelForm, PlanForm, \
    UserForm, TrxForm, PlanDurationForm, ServiceTypeForm, ProviderPriceForm
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, UpdateView, DeleteView
from django.views import generic
from django.views.generic.edit import View
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.db import connections
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.forms import inlineformset_factory
from django.views.generic import ListView, CreateView, DetailView
from django.core.paginator import Paginator
import numpy as np
from datetime import datetime

def createAccountExchange(request):
    customerConf = models.CustomerConfig(customer_id=request.user.id)
    form = CustomerConfigForm(instance=customerConf)

    if request.method == 'POST':
        form = CustomerConfigForm(request.POST or None, instance=customerConf)

        if form.is_valid():
            print(5 * " createAccountExchange")
            cconf = form.save(commit=False)
            cconf.created=datetime.now()
            cconf.updated=datetime.now()
            cconf.save()
            return redirect('edit-customer',id = request.user.id)
        else:
            print(form.errors)
    context = {'form': form}
    return render(request, 'edit_account_exchange.html', context)

class DeleteAccountExchange(LoginRequiredMixin, DeleteView):
    model = models.CustomerConfig
    print('deleteeeeeeee')
    template_name = 'partials/delete_confirm_inline.html'
    # to do
    # you should change it to previous page
    success_url = '/'

class EditAccountExchange(LoginRequiredMixin, UpdateView):
    model =  models.CustomerConfig
    fields = '__all__'
    template_name = 'edit_account_exchange.html'
    # to do
    # you should change it to previous page
    success_url = '/'
'''
def editAccountExchange(request, id):
    customerConfig = models.CustomerConfig.objects.get(id=id)
    form = CustomerConfigForm(request.POST or None,instance=customerConfig)
    if request.method == 'POST':
        form = CustomerConfigForm(request.POST or None,  instance=customerConfig)
        if form.is_valid():
            print(5 * " Update")
            form.save();
            # messages.success(request, 'Your profile is updated successfully')
            return redirect('edit-customer',id=id)
        else:
            print(form.errors)
    context = {'form': form}
    return render(request, 'edit_account_exchange.html', context)
'''

def EditCustomerView(request, id):
    customer = models.Customer.objects.get(id=request.user.id)
    form = CustomerForm(instance=customer)

    customerConfig = customer.customerconfig_set.all().order_by('-id');

    if request.method == 'POST':
        # customer.status = request.POST.get('status')
        form = CustomerForm(request.POST  or None, request.FILES, instance=customer)
        if form.is_valid():
            print(5 * " EditCustomerView")
            form.save();
            messages.success(request, 'Your profile is updated successfully')
            return redirect('home')
        else:
            print(form.errors)
    context = {'form': form, 'customerConfig': customerConfig}
    return render(request, 'edit_customer.html', context)
    # return render(request, 'test.html', context)


def test(request):
    return render(request, 'public/index.html', {})


def EditCustomerConfigView(request, id):
    customerConfig = models.CustomerConfig.objects.get(customer_id=id)
    form = CustomerConfigForm(request.POST  or None,instance=customerConfig)

    if request.method == 'POST':
        form = CustomerConfigForm(request.POST , instance=customerConfig)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form_row': form, 'customerConfig': customerConfig, 'numberTp': 'numberTpForm'}
    return render(request, 'edit_customer_config.html', context)


def userProfile(request, pk):
    cusotmer = models.Customer.objects.get(id_id=pk)
    context = {'cusotmer': cusotmer}
    return render(request, 'profile.html', context)


def home(request):
    if request.user.is_authenticated:
        customer = models.Customer.objects.get(id_id=request.user.id)
        context = {'customer': customer}
    else:
        context = {}
    return render(request, 'home.html', context)


@login_required(login_url='login')
def createCustomer(request):
    form = CustomerForm
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            # form.save()
            cusotmer = form.save(commit=False)  # commit next
            cusotmer.id_id = request.user.id
            # cusotmer.phone = form.phone
            cusotmer.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'custom_form.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username Or Password does not exist')

    context = {'page': page}
    # return render(request, 'public/login.html', context)
    return render(request, 'public/login_page.html', context)


def registerPage(request):
    page = 'signup'
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            print("form is valid")
            user = form.save(commit=False)
            user.username = user.username.lower()
            username = user.username
            raw_password = form.cleaned_data.get('password1')
            user.save()
            user = authenticate(username=username, password=raw_password)

            customer = models.Customer(id_id=user.id, first_name=form.cleaned_data['first_name'],
                                       last_name=form.cleaned_data['last_name'],
                                       # phone=form.cleaned_data['phone'],
                                       status=1,
                                       email=form.cleaned_data['email'])
            customer.save()
            login(request, user)
            return redirect('home')
        else:
            print("form is NOT valid")
            messages.error(request, 'An error occured during registration')

    context = {'page': page, 'form': form}
    return render(request, 'public/signup.html', context)


class provider_activity(ListView):
    # model = Signal
    paginate_by = 20
    context_object_name = 'provider_acitivties'
    template_name = 'vendor_activity_sum.html'

    # template_name = 'provider_radarchart.html'
    def get_queryset(self):
        try:
            with connections['default'].cursor() as cursor:
                cursor.execute(f"select  a.id, avatar, a.name, profit_all, b.loss_all, a.created, b.rank "
                               f"from provider a, provider_activity b where a.id = b.provider_id order by rank desc")
                return dictfetchall(cursor)
        except:
            print('None')
            context = {'provider_acitivties': 'None'}
            return context


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def vendorProfile(request, id):
    try:
        with connections['default'].cursor() as cursor:
            cursor.execute(f"select * from v_provider where id={id}")
            provider_profile = dictfetchall(cursor)
            chartLabel = ['last day', 'last 7 days', 'last 30 days', 'last 365 days', 'all']

            context = {'provider_profile': provider_profile, 'chartLabel': chartLabel}
            return render(request, 'vendor_profile.html', context)
    except:
        return HttpResponse('error')


class BetterMixin:
    template_name = 'signal_form_old.html'

    def get_template_names(self):
        if self.request.GET.get("better"):
            return ["signal_form_old.html"]
        return super().get_template_names()

    def get_success_url(self):
        return "/"


def planView(request):
    try:
        with connections['default'].cursor() as cursor:

            cursor.execute(f"select status from customer where id_id={request.user.id}")
            status = cursor.fetchall()

            cursor.execute(f"select NAME, DSC, id from plan where status=1")
            plan = cursor.fetchall()

            cursor.execute(f"select plan_name, price, pricewithdisc from plan_price where status=1")
            plan_price = cursor.fetchall()

            cursor.execute(f"select name,status, plan_id  from plan_feature ")
            plan_feature = cursor.fetchall()

            context = {'plan': plan, 'plan_price': plan_price, 'plan_feature': plan_feature, 'status': status[0][0]}
            return render(request, 'plan.html', context)
    except:
        return HttpResponse('error')


def extendPlan_aj(request, id):
    plan_duration = PlanDurationForm(request.GET)
    # plan = models.PlanPrice.objects.get(plan_id=id, planDuration_id=1)
    plan_name = PlanForm(request.GET)
    service_name = ServiceTypeForm(request.GET)
    provider_name = ProviderPriceForm(request.GET)

    context = {'plan_duration': plan_duration, 'plan_name': plan_name, 'total_price': 0, 'service_name': service_name,
               'provider_name': provider_name}
    return render(request, 'extend_plan1.html', context)


class ValidateExtendPlan(View):
    def get(self, request):
        planDure = request.GET.get('plan_duration', None)
        plan = request.GET.get('plan_name', None)
        provider = request.GET.get('provider_name', None)
        service = request.GET.get('service_name', None)
        print('$' * 50)
        print(provider)

        providerPrice = models.ProviderPrice.objects.get(provider=(models.Provider.objects.get(id=provider)),
                                                         planDuration=planDure, status=1)
        planPrice = models.PlanPrice.objects.get(plan_id=plan, planDuration_id=planDure)

        print('*' * 50)
        print(service)
        total_price = providerPrice.price + planPrice.price
        total_price_with_disc = providerPrice.priceWithDisc + planPrice.priceWithDisc

        # service_name = 0 if service ==1 else  planPrice.priceWithDisc

        if service == '1':
            service_name = 'Only Signal Alerts(No auto trade)'
        else:
            service_name = 'Auto trade+Signal Alert'
        data = {
            'planPrice': planPrice.price,
            'price_with_disc': planPrice.priceWithDisc,
            'planPrice_id': planPrice.id,
            'service_name': service_name,
            'total_price': total_price,
            'total_price_with_disc': total_price_with_disc,
            'provider_name': providerPrice.price,
            'provider_name_disc': providerPrice.priceWithDisc
        }
        return JsonResponse(data)


def extendPlan(request, id):
    plan = PlanDurationForm(request.GET)
    if request.GET:
        if plan.is_valid():
            # print(plan.cleaned_data['planDuration'].id)
            planPrice = models.PlanPrice.objects.get(plan_id=id, planDuration_id=plan.cleaned_data['planDuration'].id)
            price_id = planPrice.id
            context = {'plan': plan, 'planPrice': planPrice, 'price_id': price_id}

            return render(request, 'extend_plan.html', context)

    context = {'plan': plan, 'price_id': 1}
    return render(request, 'extend_plan.html', context)


class invoiceDetailView(UpdateView):
    model = models.Invoice
    fields = '__all__'
    template_name = 'invoice_form.html'
    success_url = '/invoice-list/'

    def form_valid(self, form, **kwargs):
        print('Valid '*10)
        form.instance.id = self.kwargs['pk']
        form.instance.updated = datetime.now()
        return super().form_valid(form)

def invoiceRegisterView(request, pr, tpr):
    planPrice = models.PlanPrice.objects.get(id=pr)
    customer = models.Customer.objects.get(id_id=request.user.id)
    print("---" * 20)
    print(pr)
    print(tpr)
    trx = models.Invoice(
        trx_id=0
        , status=1
        , w_customer=request.user.username + '___Wallet'
        , customer_id=request.user.id
        , PlanPrice_id=pr
        , total_price=tpr)

    form = TrxForm(instance=trx)

    if request.method == 'POST':
        form = TrxForm(request.POST, instance=trx)

        if form.is_valid():
            print('valid '*10)
            temp = form.save(commit=False)
            if form.cleaned_data['trx_id'] == '100':
                temp.status = 2
            else:
                temp.status = 3
                print('Wrong Trx number...')
            temp.save()
            return HttpResponseRedirect('/invoice-list')
        else:
            print(form.errors.as_data())
    context = {'form': form, 'planPrice': planPrice}

    return render(request, 'invoice_form.html', context)


@login_required(login_url='login')
def invoiceList(request):
    invoice = models.Invoice.objects.filter(customer_id=request.user.id).order_by('-id')
    context = {'form': invoice}

    return render(request, 'invoice_list.html', context)


@login_required(login_url='login')
def dashbord(request):
    account = models.CustomerConfig.objects.filter(customer_id=request.user.id).order_by('-id')

    try:
        with connections['default'].cursor() as cursor:
            cursor.execute(f"select  symb,status,updated from signal_order where customer_id={request.user.id}")
            result = cursor.fetchall()
            customer_order = [list(i) for i in result]
            cursor.execute(f"select symb,status,updated from signal_order where status = 1")
            top_order = cursor.fetchall()
            cursor.execute(f"select * from v_top_ex")
            topExchange = cursor.fetchall()

    except:
        return HttpResponse('error')
    context = {'account': account, 'customer_order': customer_order, 'top_order': top_order, 'topExchange': topExchange}

    return render(request, 'dashbord.html', context)


def index(request):
    account = models.CustomerConfig.objects.filter(customer_id=request.user.id).order_by('-id')

    try:
        with connections['default'].cursor() as cursor:
            cursor.execute(f"select  symb,status,updated from signal_order where customer_id={request.user.id}")
            result = cursor.fetchall()
            customer_order = [list(i) for i in result]
            cursor.execute(f"select symb,status,updated from signal_order where status = 1")
            top_order = cursor.fetchall()
    except:
        return HttpResponse('error')
    context = {'account': account, 'customer_order': customer_order, 'top_order': top_order}

    return render(request, 'index.html', {})

def aboutUs(request):
    context = {}
    return render(request, 'about.html', context)
