# Stubs for django.contrib.gis.db.backends.base.operations (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class BaseSpatialOperations:
    truncate_params = ...  # type: Any
    postgis = ...  # type: bool
    spatialite = ...  # type: bool
    mysql = ...  # type: bool
    oracle = ...  # type: bool
    spatial_version = ...  # type: Any
    select = ...  # type: Any
    geography = ...  # type: bool
    geometry = ...  # type: bool
    area = ...  # type: bool
    bounding_circle = ...  # type: bool
    centroid = ...  # type: bool
    difference = ...  # type: bool
    distance = ...  # type: bool
    distance_sphere = ...  # type: bool
    distance_spheroid = ...  # type: bool
    envelope = ...  # type: bool
    force_rhr = ...  # type: bool
    mem_size = ...  # type: bool
    num_geom = ...  # type: bool
    num_points = ...  # type: bool
    perimeter = ...  # type: bool
    perimeter3d = ...  # type: bool
    point_on_surface = ...  # type: bool
    polygonize = ...  # type: bool
    reverse = ...  # type: bool
    scale = ...  # type: bool
    snap_to_grid = ...  # type: bool
    sym_difference = ...  # type: bool
    transform = ...  # type: bool
    translate = ...  # type: bool
    union = ...  # type: bool
    disallowed_aggregates = ...  # type: Any
    geom_func_prefix = ...  # type: str
    function_names = ...  # type: Any
    unsupported_functions = ...  # type: Any
    geohash = ...  # type: bool
    geojson = ...  # type: bool
    gml = ...  # type: bool
    kml = ...  # type: bool
    svg = ...  # type: bool
    from_text = ...  # type: bool
    from_wkb = ...  # type: bool
    def convert_extent(self, box, srid): ...
    def convert_extent3d(self, box, srid): ...
    def convert_geom(self, geom_val, geom_field): ...
    def geo_quote_name(self, name): ...
    def geo_db_type(self, f): ...
    def get_distance(self, f, value, lookup_type): ...
    def get_geom_placeholder(self, f, value, compiler): ...
    def check_expression_support(self, expression): ...
    def spatial_aggregate_name(self, agg_name): ...
    def spatial_function_name(self, func_name): ...
    def geometry_columns(self): ...
    def spatial_ref_sys(self): ...
