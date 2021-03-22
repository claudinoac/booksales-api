from dataclasses import field
from typing import List

from marshmallow import validate
from marshmallow_dataclass import dataclass


@dataclass(frozen=True)
class CreateSaleCommand:
    customer: int = field(metadata=dict(validate=validate.Range(min=1)))
    books: List[int] = field(metadata=dict(validate=validate.Length(min=1, max=10)))
