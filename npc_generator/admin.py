from django.contrib import admin

# Register your models here.
from .models import CharClass, WeaponProficiencyList, Weapon, ArmourProficiencyList, Armour, ListedWeapon, ListedArmour

class ListedWeaponInline(admin.TabularInline):
    model = ListedWeapon
    extra = 3


class WeaponProfsAdmin(admin.ModelAdmin):
    inlines = [ListedWeaponInline]


class ListedArmourInline(admin.TabularInline):
    model = ListedArmour
    extra = 3


class ArmourAdmin(admin.ModelAdmin):
    list_display = ('armour_name', 'armour_type', 'armour_ac', 'armour_max_dex')
    list_filter = ['armour_type']

class ArmourProfsAdmin(admin.ModelAdmin):
    inlines = [ListedArmourInline]


class WeaponAdmin(admin.ModelAdmin):
    list_display = ('weapon_name', 'weapon_type', 'weapon_mel_range')
    list_filter = ['weapon_type']

admin.site.register(CharClass)
admin.site.register(WeaponProficiencyList, WeaponProfsAdmin)
admin.site.register(Weapon, WeaponAdmin)
admin.site.register(ArmourProficiencyList, ArmourProfsAdmin)
admin.site.register(Armour, ArmourAdmin)