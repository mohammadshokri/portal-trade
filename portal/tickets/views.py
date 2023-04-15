from django.views.generic.edit import CreateView, UpdateView, DeleteView
from tickets.models import Ticket, TicketDetail, TicketSubject
from django.views.generic import ListView
from .forms import TicketForm, TicketSubjectForm, TicketDetailForm
from django.shortcuts import get_object_or_404, redirect
from django.db import connections
from datetime import datetime


class TicketUpdateView(UpdateView):
    model = TicketDetail
    form_class = TicketDetailForm
    template_name = "ticket_form.html"
    success_url = "/tickets/"

    def get_context_data(self, **kwargs):
        context = super(TicketUpdateView, self).get_context_data(**kwargs)
        t_detail = TicketDetail.objects.filter(
            id=self.kwargs.get("pk")
        ).last()
        t = Ticket.objects.get(id=t_detail.ticket_id)
        t_subjet = TicketSubject.objects.get(id=t.ticketSubject_id)
        context["ticket_title"] = t_subjet
        context["t_detail"] = t_detail

        return context


class TicketDetailExtendView(CreateView):
    model = TicketDetail
    # form_class = TicketDetailForm
    fields = ["req"]
    template_name = "ticket_form.html"
    success_url = "/tickets/"

    def get_context_data(self, **kwargs):
        context = super(TicketDetailExtendView, self).get_context_data(
            **kwargs
        )
        print(self.kwargs["pk"])
        # prev_ticket = TicketDetail.objects.filter(ticket=TicketDetail.objects.get(id=self.kwargs['pk']).ticket)
        prev_ticket = TicketDetail.objects.filter(
            ticket=self.kwargs["pk"]
        ).values()
        print(prev_ticket)
        context = {"prev_ticket": prev_ticket, "form": TicketDetailForm}
        return context

    def form_valid(self, form, **kwargs):
        # t = TicketDetail.objects.get(ticket=self.kwargs['pk'])
        form.instance.ticket_id = self.kwargs["pk"]
        form.instance.updated = datetime.now()
        return super().form_valid(form)


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


class TicketListView(ListView):
    model = Ticket
    paginate_by = 4
    ordering = "-updated"
    context_object_name = "t_detail"
    template_name = "ticket_list.html"

    def get_queryset(self):
        try:
            with connections["default"].cursor() as cursor:
                cursor.execute(
                    f"select  t_id, dt_id, req , resp ,status, priority, created,updated  from v_ticket where user_id={self.request.user.id}"
                )
                return dictfetchall(cursor)
        except:
            print("Except None")
            context = {"t_detail": "None"}
            return context


class TicketCreateView(CreateView):
    form_class = TicketForm
    template_name = "ticket_create.html"
    success_url = "/tickets/"

    def get_context_data(self, **kwargs):
        context = super(TicketCreateView, self).get_context_data(**kwargs)
        context = {"form": TicketForm, "form_detail": TicketDetailForm}
        return context

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        ticket_detail = TicketDetailForm(self.request.POST)

        if form.is_valid() and ticket_detail.is_valid():
            return self.form_valid(form, ticket_detail)
        else:
            print("form.errors")
            return self.form_invalid(form, ticket_detail)

    def form_valid(self, form, ticket_detail):
        self.object = form.save(commit=False)
        form.instance.user = self.request.user.customer
        form.instance.status = "Open"
        form.instance.updated = datetime.now()
        form.instance.created = datetime.now()
        self.object.save()
        t_dt = ticket_detail.save(commit=False)
        t_dt.ticket = self.object
        t_dt.updated = datetime.now()
        t_dt.created = datetime.now()
        t_dt.save()
        return redirect("/tickets/")

    def form_invalid(self, form, ticket_detail_formset):
        return self.render_to_response(
            self.get_context_data(form=form, ticket_detail=ticket_detail)
        )
