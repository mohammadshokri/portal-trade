from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("register/", views.registerPage, name="register"),
    path("", views.dashbord, name="home"),
    path("profile/<str:pk>", views.userProfile, name="user-profile"),
    path("vendors/", views.provider_activity.as_view(), name="list-vendors"),
    path(
        "edit-customer/<int:id>", views.EditCustomerView, name="edit-customer"
    ),
    path(
        "edit-customer-config/<int:id>",
        views.EditCustomerConfigView,
        name="edit-customer-config",
    ),
    path(
        "vendor-profile/<int:id>", views.vendorProfile, name="vendor-profile"
    ),
    path("plan/", views.planView, name="plan"),
    path("extend-plan/<int:id>", views.extendPlan_aj, name="extend-plan"),
    path(
        "ajax/extend-plan/",
        views.ValidateExtendPlan.as_view(),
        name="extend-plan-ajax",
    ),
    # path('invoice-form/<int:planPrice_id>/<int:total_price>', views.invoiceForm, name="invoice-form"),
    # path(r'^invoice-form/(?P<pr>\d+)(?:/(?P<tpr>\d+))?', views.invoiceDetailView, name="invoice-form"),
    # path(r'^invoice-form/(?P<pr>\d+)(?:/(?P<tpr>\d+))?', views.invoiceDetailView, name="invoice-form"),
    path(
        "invoice-form/<str:pr>/<str:tpr>",
        views.invoiceRegisterView,
        name="invoice-form",
    ),
    path(
        "<int:pk>/edit",
        views.invoiceDetailView.as_view(),
        name="invoice-edit",
    ),
    # (r'^question/(?P<pk>\d+)(?:/(?P<npk>\d+))?
    path("invoice-list/", views.invoiceList, name="invoice-list"),
    path("dashbord/", views.dashbord, name="dashbord"),
    path("index/", views.index, name="index"),
    # path('ticket/', views.createTicket, name="ticket"),
    # path('ticket/', views.ticketList, name="ticket"),
    path("about/", views.aboutUs, name="about"),
    path("test", views.test, name="test"),
    # path('edit-account/<int:id>', views.editAccountExchange, name='edit-account'),
    path(
        "account/<int:pk>/edit",
        views.EditAccountExchange.as_view(),
        name="edit-account",
    ),
    path(
        "account/<int:pk>/delete",
        views.DeleteAccountExchange.as_view(),
        name="delete-account",
    ),
    path(
        "create-account", views.createAccountExchange, name="create-account"
    ),
]
