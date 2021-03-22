from dataclasses import field
from marshmallow_dataclass import dataclass
from marshmallow import validate
from typing import List


@dataclass(frozen=True)
class CreateSaleCommand:
    customer: int = field(metadata=dict(validate=validate.Range(min=1)))
    books: List[int] = field(metadata=dict(validate=validate.Length(min=1, max=10)))
