# -*- coding: utf-8 -*-
from django.contrib import admin

from core.models import Doctor, Entry


class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active',)
    search_fields = ('name',)

admin.site.register(Doctor, DoctorAdmin)


class EntryAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'start_at', 'patient',)
    search_fields = ('patient',)
    list_filter = ('doctor', 'start_at',)

admin.site.register(Entry, EntryAdmin)