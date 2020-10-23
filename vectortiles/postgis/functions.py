from django.contrib.gis.db.models import GeometryField
from django.contrib.gis.db.models.functions import GeoFunc
from django.db.models import Func
from django.utils.functional import cached_property


class RawGeometryField(GeometryField):
    def select_format(self, compiler, sql, params):
        """
        Override compiler format to not cast as bytea.
        AsMVTGeom is used in a custom sql raw. Generated queryset should not be executed without that.
        """
        print(sql, params)
        return sql, params


class MakeEnvelope(Func):
    function = "ST_MAKEENVELOPE"
    output_field = GeometryField()


class AsMVTGeom(GeoFunc):
    function = "ST_ASMVTGEOM"

    @cached_property
    def output_field(self):
        return RawGeometryField()
