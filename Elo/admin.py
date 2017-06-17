from django.contrib import admin

# Register your models here.
from .models import Rating


class RatingAdmin(admin.ModelAdmin):
    class Meta:
        model = Rating


admin.site.register(Rating, RatingAdmin)
