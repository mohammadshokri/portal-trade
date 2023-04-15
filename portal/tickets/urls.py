from django.urls import path
from . import views

app_name = "tickets"
urlpatterns = [
    path("", views.TicketListView.as_view(), name="ticket-list"),
    path("create", views.TicketCreateView.as_view(), name="ticket-create"),
    path(
        "<int:pk>/add",
        views.TicketDetailExtendView.as_view(),
        name="ticket-add",
    ),
]
