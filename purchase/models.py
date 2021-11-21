from django.db import models

# Create your models here.
class Order(models.Model):
    #item_id = models.CharField(max_length=11)
    order_first_name = models.CharField(max_length=30)
    order_last_name = models.CharField(max_length=30)
    order_email = models.CharField(max_length=50)
    order_wallet_address = models.CharField(max_length=128)
    order_street_address = models.CharField(max_length=100, default="street address", blank=True)
    order_city_address = models.CharField(max_length=100, default="city address", blank=True)
    order_region_address = models.CharField(max_length=100, default="region address", blank=True)
    order_postal_address = models.CharField(max_length=100, default="postal address", blank=True)
    order_country_address = models.CharField(max_length=100, default="country address", blank=True)
    order_notes = models.CharField(max_length=256, default="notes", blank=True, null=True)
    order_start = models.DateTimeField('date published')
    order_end = models.DateTimeField(default=None, blank=True, null=True)
    order_price = models.CharField(max_length=10)
    order_paid = models.CharField(max_length=20)
    order_status = models.CharField(max_length=20, default="incomplete", blank=True)
    wallet_balance = models.CharField(max_length=128, default="0", blank=True, null=True)
