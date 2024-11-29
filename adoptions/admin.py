from django.contrib import admin
from .models import GuineaPig, Adoption


# Register your models here.
class GuineaPigAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_year', 'gender', 'adopted')
    list_filter = ('gender', 'adopted')
    search_fields = ('name', 'birth_year')
    ordering = ('name',)


class AdoptionAdmin(admin.ModelAdmin):
    list_display = (
        'guinea_pig', 'adopter', 'address', 'phone_number',
        'number_of_guinea_pigs', 'living_arrangement'
    )
    list_filter = ('living_arrangement',)
    search_fields = ('guinea_pig__name', 'adopter__username')
    ordering = ('-guinea_pig',)


admin.site.register(GuineaPig, GuineaPigAdmin)
admin.site.register(Adoption, AdoptionAdmin)

