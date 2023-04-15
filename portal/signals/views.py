from django.views.generic.edit import CreateView
from django.views.generic import ListView
from .models import Signal, MarketPrice, SignalDt
from .form import SignalForm, SignalDetailInlineFormset
from django.views.generic.edit import View
from django.shortcuts import get_object_or_404, redirect
from django.db import connections
from datetime import datetime


class SignalDetailView(ListView):
    model = SignalDt
    paginate_by = 15

    context_object_name = "signal_detail"
    template_name = "signal_detail.html"

    def get_context_data(self, **kwargs):
        context = super(SignalDetailView, self).get_context_data(**kwargs)
        s_detail = (
            SignalDt.objects.filter(signal=self.kwargs["pk"])
            .values()
            .order_by("tp")
        )

        context = {"signal_detail": s_detail}
        return context


class SignalListView(ListView):
    model = Signal
    paginate_by = 15
    ordering = "-id"
    context_object_name = "signals"
    template_name = "signal_list.html"

    def get_queryset(self):
        try:
            with connections["default"].cursor() as cursor:
                print(self.request.user.id)
                cursor.execute(
                    f"select id, id_id, typ,side, lv, ep1, ep2,ep3,ep4, sl_number ,ex_name, updated, created, provider_name,avatar,status  from v_signal where id_id={self.request.user.id}"
                )
                return dictfetchall(cursor)

        except:
            print("None")
            context = {"signals": "None"}
            return context


class SignalSpotListView(ListView):
    model = Signal
    paginate_by = 15
    ordering = "-id"
    context_object_name = "signals"
    template_name = "signal_list_spot.html"

    def get_queryset(self):
        try:
            with connections["default"].cursor() as cursor:
                print(self.request.user.id)
                cursor.execute(
                    f"select id, id_id, typ,side,lv, ep1, ep2,ep3,ep4, sl_number ,ex_name, updated, created, provider_name,avatar,status  from v_signal where id_id={self.request.user.id}"
                )
                return dictfetchall(cursor)

        except:
            print("None")
            context = {"signals": "None"}
            return context


class SignalFutureListView(ListView):
    model = Signal
    paginate_by = 15
    ordering = "-id"
    context_object_name = "signals"
    template_name = "signal_list_future.html"

    def get_queryset(self):
        try:
            with connections["default"].cursor() as cursor:
                print(self.request.user.id)
                cursor.execute(
                    f"select id, id_id, typ,side,lv, ep1, ep2,ep3,ep4, sl_number ,ex_name, updated, created, provider_name,avatar,status  from v_signal where id_id={self.request.user.id}"
                )
                return dictfetchall(cursor)

        except:
            print("None")
            context = {"signals": "None"}
            return context


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


class SignalCreateView(CreateView):
    form_class = SignalForm
    template_name = "signal_form.html"

    def get_context_data(self, **kwargs):
        context = super(SignalCreateView, self).get_context_data(**kwargs)
        # context["provider"]= models.Provider.objects.get(id=1)
        if self.request.POST:
            context["signal_detail_formset"] = SignalDetailInlineFormset(
                self.request.POST
            )
        else:
            context["signal_detail_formset"] = SignalDetailInlineFormset()
        return context

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        signal_detail_formset = SignalDetailInlineFormset(self.request.POST)

        if form.is_valid() and signal_detail_formset.is_valid():
            return self.form_valid(form, signal_detail_formset)
        else:
            print(form.errors)
            print(signal_detail_formset.errors)
            return self.form_invalid(form, signal_detail_formset)

    def form_valid(self, form, signal_detail_formset):
        self.object = form.save(commit=False)
        form.instance.provider_id = 1
        form.instance.updated = datetime.now()
        form.instance.created = datetime.now()
        self.object.save()
        # saving ProductMeta Instances
        signal_metas = signal_detail_formset.save(commit=False)
        # print(signal_metas.count())
        for meta in signal_metas:
            print("*")
            meta.signal = self.object
            meta.updated = datetime.now()
            meta.created = datetime.now()
            meta.save()
        # return redirect(reverse("product:product_list"))
        return redirect("home")

    def form_invalid(self, form, signal_detail_formset):
        return self.render_to_response(
            self.get_context_data(
                form=form, signal_detail_formset=signal_detail_formset
            )
        )


class GetExchangePriceView(View):
    def get(self, request):
        p_exchange = request.GET.get("p_exchange", None)
        exchangePrice = MarketPrice.objects.get(name=p_exchange)
        data = {
            "p_exchange": exchangePrice.prc,
        }
        return JsonResponse(data)
