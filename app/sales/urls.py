from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from app.sales import views

urlpatterns = [
    url(r'^sale/$',
        views.SaleList.as_view(),
        name='sale-list'),
    url(r'^sale/(?P<pk>[0-9a-f-]+)/$',
        views.SaleDetail.as_view(),
        name='sale-detail'),
    url(r'^sale/active/(?P<pk>[0-9a-f-]+)/$',
        views.SaleActiveDetail.as_view(),
        name='sale-active-detail'),
    url(r'^sale/paymentmethod/$',
        views.PaymentMethodList.as_view(),
        name='paymentmethod-list'),
    url(r'^sale/paymentmethod/(?P<pk>[0-9a-f-]+)/$',
        views.PaymentMethodDetail.as_view(),
        name='paymentmethod-detail'),
    ]

urlpatterns = format_suffix_patterns(urlpatterns)
