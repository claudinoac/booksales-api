from dataclasses import field
from decimal import Decimal
from marshmallow_dataclass import dataclass
from marshmallow import validate


@dataclass(frozen=True)
class CreateBookCommand:
    title: str = field(metadata=dict(validate=validate.Length(min=3, max=250)))
    year: int = field(metadata=dict(validate=validate.Range(min=0, max=32767)))
    price: Decimal = field(metadata=dict(validate=validate.Range(min=0)))
    author: str = field(metadata=dict(validate=validate.Length(min=3, max=250)))
    ISBN: int = field(metadata=dict(validate=validate.Range(min=0)))
    language: str = field(metadata=dict(validate=validate.Length(min=3, max=250)))
