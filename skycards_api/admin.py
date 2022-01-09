from django.contrib import admin
from skycards_api.models import Card


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    pass
