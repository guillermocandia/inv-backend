from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from app.report import views

urlpatterns = [
    url(r'^report/sale/$',
        views.ReportSaleList.as_view(),
        name='report-sale-list'),
    ]

urlpatterns = format_suffix_patterns(urlpatterns)
