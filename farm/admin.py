from django.contrib import admin
from . import models

class FarmAdmin(admin.ModelAdmin):
    list_display = ("name", "farm_type")


class FarmerAdmin(admin.ModelAdmin):
    list_display = ("first_name", "surname", "user")


class FarmFarmerLinkerAdmin(admin.ModelAdmin):
    list_display = ("farm", "farmer", "started_on", "stopped_on")


class FieldAdmin(admin.ModelAdmin):
    list_display = ("name", "size")


class FarmFieldLinkerAdmin(admin.ModelAdmin):
    list_display = ("farm", "field", "acquired_on", "removed_on")


admin.site.register(models.Farm, FarmAdmin)
admin.site.register(models.Farmer, FarmerAdmin)
admin.site.register(models.FarmFarmerLinker, FarmFarmerLinkerAdmin)
admin.site.register(models.Field, FieldAdmin)
admin.site.register(models.FarmFieldLinker, FarmFieldLinkerAdmin)

