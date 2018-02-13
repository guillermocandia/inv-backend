from rest_framework import serializers


class ReportSaleSerializer(serializers.Serializer):
    url = serializers.URLField()
