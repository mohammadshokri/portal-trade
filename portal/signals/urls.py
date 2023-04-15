from django.urls import path
from . import views

app_name = "signals"
urlpatterns = [
    path(
        "create-signal/",
        views.SignalCreateView.as_view(),
        name="create-signal",
    ),
    path(
        "detail/<int:pk>",
        views.SignalDetailView.as_view(),
        name="signal-detail",
    ),
    path("", views.SignalListView.as_view(), name="list-signal"),
    path("spot", views.SignalSpotListView.as_view(), name="list-signal-spot"),
    path(
        "future",
        views.SignalFutureListView.as_view(),
        name="list-signal-future",
    ),
    path(
        "ajax/create-signal/",
        views.GetExchangePriceView.as_view(),
        name="create-signal-ajax",
    ),
]
