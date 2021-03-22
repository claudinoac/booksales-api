from apps.base.serializers import BaseSerializer


class CustomerSerializer(BaseSerializer):
    fields = ["id", "first_name", "last_name", "email", "phone"]
