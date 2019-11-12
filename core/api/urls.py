from django.urls import path

from .views import *

urlpatterns = [
    path('userprofile', UserProfileListView.as_view()),
    path('userprofile/<pk>', UserProfileDetailView.as_view()),

    path('item', ItemListView.as_view()),
    path('item/<pk>', ItemDetailView.as_view()),

    path('orderitem', OrderItemListView.as_view()),
    path('orderitem/<pk>', OrderItemDetailView.as_view()),

    path('order', OrderListView.as_view()),
    path('order/<pk>', OrderDetailView.as_view()),

    path('address', AddressListView.as_view()),
    path('address/<pk>', AddressDetailView.as_view()),

    path('payment', PaymentListView.as_view()),
    path('payment/<pk>', PaymentDetailView.as_view()),

    path('coupon', CouponListView.as_view()),
    path('coupon/<pk>', CouponDetailView.as_view()),

    path('refund', RefundListView.as_view()),
    path('refund/<pk>', RefundDetailView.as_view()),
]
