from decimal import Decimal

class SerializerError(Exception):
    pass

class BaseSerializer:
    fields = []
    instance = None
    multiple = False

    def __init__(self, instance, multiple=False):
        if not self.is_serializable(instance, multiple):
            raise SerializerError(
                "Instance of type {} is not serializable by {}".format(
                    instance.__class__.__name__, self.__class__.__name__
                )
            )
        self.instance = instance
        self.multiple = multiple

    def is_serializable(self, instance, multiple):
        instance_to_test = instance[0] if multiple else instance
        for field in self.fields:
            if not hasattr(instance_to_test, field):
                return False
        return True

    def _serialize_data_as_dict(self, data_object):
        dict_data = {}
        for field in self.fields:
            field_data = getattr(data_object, field)
            if isinstance(field_data, Decimal):
                field_data = "%.2f" % field_data
            dict_data.update({
                field: field_data
            })
        return dict_data

    def as_dict(self):
        if self.multiple:
            aggregated_data = {"items": []}
            for instance in self.instance:
                aggregated_data["items"].append(self._serialize_data_as_dict(instance))
            return aggregated_data
        return self._serialize_data_as_dict(self.instance)
