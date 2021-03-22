from decimal import Decimal

from sqlalchemy.orm.collections import InstrumentedList

from apps.base.serializers import BaseSerializer


class SaleSerializer(BaseSerializer):
    fields = ["id", "customer_id", "books", "total_value", "charged_value", "applied_discount"]

    def _serialize_data_as_dict(self, data_object):
        dict_data = {}
        for field in self.fields:
            field_data = getattr(data_object, field)
            if isinstance(field_data, Decimal):
                field_data = "%.2f" % field_data
            if isinstance(field_data, InstrumentedList):
                field_data = [item.id for item in field_data]
            dict_data.update({field: field_data})
        return dict_data
