from rest_framework import serializers

from .models import Area


class AreaAddressSerializer(serializers.ModelSerializer):
    """
    上级行政区序列化器
    """
    class Meta:
        model = Area
        fields = ('id', 'name')


class SubAreaAddressSerializer(serializers.ModelSerializer):
    """
    子级行政区序列化器
    """
    subs = AreaAddressSerializer(many=True, read_only=True)
    class Meta:
        model = Area
        fields = ('id', 'name', 'subs')

