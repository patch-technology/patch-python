# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from patch_api.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from patch_api.model.allocation import Allocation
from patch_api.model.create_bitcoin_estimate_request import CreateBitcoinEstimateRequest
from patch_api.model.create_ethereum_estimate_request import (
    CreateEthereumEstimateRequest,
)
from patch_api.model.create_flight_estimate_request import CreateFlightEstimateRequest
from patch_api.model.create_mass_estimate_request import CreateMassEstimateRequest
from patch_api.model.create_order_request import CreateOrderRequest
from patch_api.model.create_shipping_estimate_request import (
    CreateShippingEstimateRequest,
)
from patch_api.model.create_success_response import CreateSuccessResponse
from patch_api.model.create_vehicle_estimate_request import CreateVehicleEstimateRequest
from patch_api.model.error_response import ErrorResponse
from patch_api.model.estimate import Estimate
from patch_api.model.estimate_list_response import EstimateListResponse
from patch_api.model.estimate_response import EstimateResponse
from patch_api.model.highlight import Highlight
from patch_api.model.meta_index_object import MetaIndexObject
from patch_api.model.order import Order
from patch_api.model.order_list_response import OrderListResponse
from patch_api.model.order_response import OrderResponse
from patch_api.model.parent_technology_type import ParentTechnologyType
from patch_api.model.photo import Photo
from patch_api.model.project import Project
from patch_api.model.project_list_response import ProjectListResponse
from patch_api.model.project_response import ProjectResponse
from patch_api.model.sdg import Sdg
from patch_api.model.standard import Standard
from patch_api.model.technology_type import TechnologyType
from patch_api.model.technology_type_list_response import TechnologyTypeListResponse
