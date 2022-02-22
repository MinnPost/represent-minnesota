from django.contrib.gis.db import models
from django.http import Http404
from django.contrib.gis.geos import GEOSGeometry
from django.utils.datastructures import MultiValueDictKeyError
from django.utils.translation import ugettext as _

from boundaries.views import BoundaryListView
from boundaries.base_views import BadRequest
from boundaries.models import BoundarySet, Boundary, app_settings


class BoundaryListView(BoundaryListView):
    filterable_fields = ['external_id', 'name']
    allowed_geo_fields = ('shape', 'simple_shape', 'centroid')
    default_geo_filter_field = 'shape'
    model = Boundary

    def filter(self, request, qs):
        qs = super(BoundaryListView, self).filter(request, qs)

        if 'intersects' in request.GET:
            try:
                (set_slug, slug) = request.GET['intersects'].split('/')
                shape = Boundary.objects.filter(slug=slug, set=set_slug).values_list('shape', flat=True)[0]
            except IndexError:
                raise Http404
            except ValueError:
                raise BadRequest(_("Invalid value for intersects filter"))
            qs = qs.filter(models.Q(shape__covers=shape) | models.Q(shape__overlaps=shape))

        if 'touches' in request.GET:
            try:
                (set_slug, slug) = request.GET['touches'].split('/')
                shape = Boundary.objects.filter(slug=slug, set=set_slug).values_list('shape', flat=True)[0]
            except IndexError:
                raise Http404
            except ValueError:
                raise BadRequest(_("Invalid value for touches filter"))
            qs = qs.filter(shape__touches=shape)

        if 'buffered_intersect' in request.GET:
            try:
              buffer_size = request.GET['buffersize']
            except MultiValueDictKeyError:
              raise BadRequest(_("Must provide buffersize argument for buffered_intersect"))
            try:
                (set_slug, slug) = request.GET['buffered_intersect'].split('/')
                shape = Boundary.objects.filter(slug=slug, set=set_slug).values_list('shape', flat=True)[0]
                buffered_shape = GEOSGeometry(shape).buffer(float(buffer_size))
            except IndexError:
                raise Http404
            except ValueError:
                raise BadRequest(_("Invalid value for buffered_intersect filter"))
            qs = qs.filter(models.Q(shape__overlaps=buffered_shape) | models.Q(shape__covers=buffered_shape))

        if 'sets' in request.GET:
            set_slugs = request.GET['sets'].split(',')
            qs = qs.filter(set__in=set_slugs)

        return qs