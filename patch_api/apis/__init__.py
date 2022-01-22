# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.estimates_api import EstimatesApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from patch_api.api.estimates_api import EstimatesApi
from patch_api.api.orders_api import OrdersApi
from patch_api.api.projects_api import ProjectsApi
from patch_api.api.technology_types_api import TechnologyTypesApi
