from apps.base.serializers import BaseSerializer


class BookSerializer(BaseSerializer):
    fields = ["id", "title", "year", "price", "author", "ISBN", "language"]
