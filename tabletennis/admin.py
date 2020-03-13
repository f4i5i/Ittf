from django.contrib import admin
from django_admin_listfilter_dropdown.filters import (
    DropdownFilter, ChoiceDropdownFilter, RelatedDropdownFilter
)

# Register your models here.
from .models import *

class PhasesAdmin(admin.ModelAdmin):
    list_display = ('key','desc','evkey','phase_type')
    list_filter = (('phase_type',DropdownFilter),
                    ('key',DropdownFilter),)

class CompAdmin(admin.ModelAdmin):
    list_display = ('champ','description','location', 'url')
    list_filter = (('location',DropdownFilter),)
    search_fields = ('champ','location','description')

class CountryAdmin(admin.ModelAdmin):
    list_display = ('name','short_name')

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name','country')

class TableAdmin(admin.ModelAdmin):
    list_display = ('key','desc')

class MatchRawAdmin(admin.ModelAdmin):    
    list_display = ('Competition_id','url')

class MatchAdmin(admin.ModelAdmin):
    list_display = ('comp_id','home_player','away_player','away_team','home_team','venue','time','table_','created_at','match','phase_')
    list_filter = (('match',DropdownFilter),)
    search_fields = ('venue',)


class MissingAdmin(admin.ModelAdmin):
    pass

admin.site.register(Competition,CompAdmin)
admin.site.register(RawData)
admin.site.register(Phases,PhasesAdmin)
admin.site.register(Table,TableAdmin)
admin.site.register(Match,MatchAdmin)
admin.site.register(Player,PlayerAdmin)
admin.site.register(Country,CountryAdmin)
admin.site.register(MatchRawData,MatchRawAdmin)
admin.site.register(Team)
admin.site.register(Missingdata)
