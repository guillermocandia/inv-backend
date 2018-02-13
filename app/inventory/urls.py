from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from app.inventory import views

urlpatterns = [
    url(r'^category/$',
        views.CategoryList.as_view(),
        name='category-list'),
    url(r'^category/(?P<pk>[0-9a-f-]+)/$',
        views.CategoryDetail.as_view(),
        name='category-detail'),
    url(r'^brand/$',
        views.BrandList.as_view(),
        name='brand-list'),
    url(r'^brand/(?P<pk>[0-9a-f-]+)/$',
        views.BrandDetail.as_view(),
        name='brand-detail'),
    url(r'^item/$',
        views.ItemList.as_view(),
        name='item-list'),
    url(r'^item/(?P<pk>[0-9a-f-]+)/$',
        views.ItemDetail.as_view(),
        name='item-detail'),
    ]

urlpatterns = format_suffix_patterns(urlpatterns)
