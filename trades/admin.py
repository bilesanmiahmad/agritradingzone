from django.contrib import admin
from trades.models import Crop, Product, Profile, Bid, Document, Sale

# Register your models here.

admin.site.register(Crop)
admin.site.register(Profile)
admin.site.register(Product)
admin.site.register(Bid)
admin.site.register(Document)
admin.site.register(Sale)
