from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import AreaAddressSerializer, SubAreaAddressSerializer
from rest_framework_extensions.cache.mixins import CacheResponseMixin

from .models import Area

class AreaViewSet(CacheResponseMixin, ReadOnlyModelViewSet):
    # 重写查询集方法
    def get_queryset(self):
        if self.action == 'list':
            return Area.objects.filter(parent=None)
        else:
            return Area.objects.all()

    # 重写序列化器类
    def get_serializer_class(self):
        if self.action == 'list':
            return AreaAddressSerializer
        else:
            return SubAreaAddressSerializer
