from django.conf.urls import include, url
from django.contrib import admin

from .views import BoundaryListView

admin.autodiscover()

urlpatterns = [
    url(r'^boundaries/$',
        BoundaryListView.as_view(),
        name='boundaries_boundary_list'),
    url(r'^boundaries/(?P<geo_field>shape|simple_shape|centroid)$',
        BoundaryListView.as_view(),
        name='boundaries_boundary_list'),
    url(r'^boundaries/(?P<set_slug>[\w_-]+)/$',
        BoundaryListView.as_view(),
        name='boundaries_boundary_list'),
    url(r'^boundaries/(?P<set_slug>[\w_-]+)/(?P<geo_field>shape|simple_shape|centroid)$',
        BoundaryListView.as_view(),
        name='boundaries_boundary_list'),
    url(r'^admin/', admin.site.urls),
    url('', include('boundaries.urls')),
    url('', include('finder.urls'))
]