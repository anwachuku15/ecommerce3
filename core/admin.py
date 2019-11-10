from django.contrib import admin
# Register your models here.
from .models import *


def accept_refund(modeladmin, request, queryset):
    queryset.update(refund_requested=False, refund_granted=True)


accept_refund.short_description = 'Accept refund requests'


# def order_en_route(modeladmin, request, queryset):
#     queryset.update(being_delivered=True)


# order_en_route.short_description = 'Being delivered'


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user',
                    'ordered',
                    'being_delivered',
                    'received',
                    'refund_requested',
                    'refund_granted',
                    'billing_address',
                    'payment',
                    'coupon'
                    ]

    list_display_links = ['user',
                          'billing_address',
                          'payment',
                          'coupon'
                          ]

    list_filter = ['ordered',
                   'being_delivered',
                   'received',
                   'refund_requested',
                   'refund_granted'
                   ]

    search_fields = [
        'user__username',
        'ref_code',
    ]

    actions = [accept_refund]


admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order, OrderAdmin)
admin.site.register(Payment)
admin.site.register(Coupon)
admin.site.register(Refund)
