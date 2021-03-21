from dataclasses import field
from marshmallow_dataclass import dataclass
from marshmallow import validate


@dataclass(frozen=True)
class CreateCustomerCommand:
    first_name: str = field(metadata=dict(validate=validate.Length(min=3, max=250)))
    last_name: str = field(metadata=dict(validate=validate.Length(min=3, max=250)))
    email: str = field(metadata=dict(validate=validate.Email()))
    phone: int = field(metadata=dict(validate=validate.Range(min=9999999)))
