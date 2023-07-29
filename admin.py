from django.contrib import admin
from .models import Advertisements

class Advertisementsadmin(admin.ModelAdmin):
    list_display = ["id", "title", "description", "price", "auction", "crated_at", "update_at"]
    list_filter = ['auction', "created_at"]
    actions = ["make_auction_as_false"]

    #Содаю функции
    @admin.action(description="Убрать возможность торга")
    def make_aution_as_false(self, request, queryset):
        print(queryset, type(queryset))
        queryset.update(auction = False)

admin.site.register()