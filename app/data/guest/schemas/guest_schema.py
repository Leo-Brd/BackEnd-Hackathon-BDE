"""Schema for serializing/deserializing a GuestModel"""

from data.guest.models.guest_model import GuestModel
from shared.utils.schema.base_schema import BaseSchema


class GuestSchema(BaseSchema):
    class Meta:
        model = GuestModel
        load_instance = True
