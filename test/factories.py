import factory
from patch_api.models.order import Order  # noqa: E501
from patch_api.models.offset import Offset  # noqa: E501
from patch_api.models.standard import Standard  # noqa: E501
from patch_api.models.estimate import Estimate  # noqa: E501
from patch_api.models.meta_index_object import MetaIndexObject  # noqa: E501
from patch_api.models.allocation import Allocation  # noqa: E501
from patch_api.models.project import Project  # noqa: E501
from patch_api.models.photo import Photo  # noqa: E501
from patch_api.models.preference import Preference  # noqa: E501
from patch_api.models.membership import Membership


class OrderFactory(factory.Factory):
    class Meta:
        model = Order

    id = "0"
    mass_g = 1
    production = True
    state = "draft"
    allocation_state = "pending"
    price_cents_usd = "0"
    patch_fee_cents_usd = "0"
    allocations = []
    metadata = {}


class StandardFactory(factory.Factory):
    class Meta:
        model = Standard

    type = "0"
    acronym = "0"
    description = "0"


class MetaIndexObjectFactory(factory.Factory):
    class Meta:
        model = MetaIndexObject

    prev_page = 56
    next_page = 56


class AllocationFactory(factory.Factory):
    class Meta:
        model = Allocation

    id = "0"
    production = True
    mass_g = 56


class EstimateFactory(factory.Factory):
    class Meta:
        model = Estimate

    id = ("0",)
    production = (True,)
    type = ("0",)
    order = OrderFactory()


class PhotoFactory(factory.Factory):
    class Meta:
        model = Photo

    id = "0"
    url = "https://photo.com"


class ProjectFactory(factory.Factory):
    class Meta:
        model = Project

    id = "0"
    production = True
    name = "0"
    description = "0"
    type = "biomass"
    country = "0"
    developer = "0"
    photos = ([PhotoFactory()],)
    average_price_per_tonne_cents_usd = 56
    remaining_mass_g = 56
    standard = StandardFactory()


class PreferenceFactory(factory.Factory):
    class Meta:
        model = Preference

    id = "0"
    allocation_percentage = 56
    project = ProjectFactory()


class OffsetFactory(factory.Factory):
    class Meta:
        model = Offset

    id = "0"
    allocated_mass_g = 0
    fulfilled_at = "0"
    fulfillment_state = "pending"
    mass_g = 1
    price_cents_usd = "0"
    production = True
    retired = True
    serial_number = "0"
    vintage_year = 56
    project_id = "0"


class MembershipFactory(factory.Factory):
    class Meta:
        model = Membership

    email = "0"
    role = "admin"
    organization_id = "0"
