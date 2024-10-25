from django.contrib import admin
from .models import GuineaPig, Adopter, Adoption

# Register your models here.


class GuineaPigAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_year', 'gender', 'adopted')
    list_filter = ('gender', 'adopted')
    search_fields = ('name', 'birth_year')
    ordering = ('name',)

@admin.register(Adopter)
class AdopterAdmin(admin.ModelAdmin):
    list_display = ('user', 'contact_number', 'address')
    search_fields = ('user__username', 'contact_number')
    ordering = ('user',)

class AdoptionAdmin(admin.ModelAdmin):
    list_display = ('guinea_pig', 'adopter', 'adoption_date')
    list_filter = ('adoption_date',)
    search_fields = ('guinea_pig__name', 'adopter__user__username')
    ordering = ('-adoption_date',)


admin.site.register(GuineaPig)
admin.site.register(Adoption)