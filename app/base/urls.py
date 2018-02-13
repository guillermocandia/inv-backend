from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from app.base import views

urlpatterns = [
    url(r'^user/$',
        views.UserList.as_view(),
        name='user-list'),
    url(r'^user/(?P<pk>[0-9]+)/$',
        views.UserDetail.as_view(),
        name='user-detail'),
    url(r'^user/password/(?P<pk>[0-9]+)/$',
        views.UserPasswordDetail.as_view(),
        name='userpassword-detail'),
    url(r'^logout/$',
        views.Logout.as_view(),
        name='logout'),
    url(r'^check-token/$',
        views.CheckToken.as_view(),
        name='check-token'),
    ]

urlpatterns = format_suffix_patterns(urlpatterns)
