from rest_framework.generics import ListAPIView, RetrieveAPIView

from core.models import *
from .serializers import *


class UserProfileListView(ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class UserProfileDetailView(RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class ItemListView(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemDetailView(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class OrderItemListView(ListAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class OrderItemDetailView(RetrieveAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class OrderListView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetailView(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class AddressListView(ListAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class AddressDetailView(RetrieveAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class PaymentListView(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class PaymentDetailView(RetrieveAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class CouponListView(ListAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer


class CouponDetailView(RetrieveAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer


class RefundListView(ListAPIView):
    queryset = Refund.objects.all()
    serializer_class = RefundSerializer


class RefundDetailView(RetrieveAPIView):
    queryset = Refund.objects.all()
    serializer_class = RefundSerializer
