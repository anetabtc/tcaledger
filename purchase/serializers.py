from rest_framework import serializers

from .models import Order

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = (
                'id',
                # 'item_id',
                'order_first_name',
                'order_last_name',
                'order_email',
                'order_wallet_address',
                'order_street_address',
                'order_city_address',
                'order_region_address',
                'order_postal_address',
                'order_country_address',
                'order_notes',
                'order_start',
                'order_end',
                'order_price',
                'order_paid',
                'order_status',
                'wallet_balance'
            )
