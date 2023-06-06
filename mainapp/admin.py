from django.contrib import admin
from .models import *


@admin.register(Poliklinika)
class PoliklinikaAdmin(admin.ModelAdmin):
    list_display = ('id', 'organization', 'address', 'phone')
    list_display_links = ('id', 'organization', 'address', 'phone')
    search_fields = ('organization', 'address')


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')
    list_display_links = ('id', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name')
    list_filter = ('poliklinika', 'position')


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone',)
    list_display_links = ('id', 'first_name', 'last_name',)
    search_fields = ('first_name', 'last_name',)
    list_filter = ('gender', 'national',)


@admin.register(Zapis)
class ZapisAdmin(admin.ModelAdmin):
    list_display = ('id', 'doctor', 'patient', 'completed')
    list_display_links = ('id', 'doctor', 'patient',)
    list_editable = ('completed',)


@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone',)
    list_display_links = ('id', 'first_name', 'last_name',)


@admin.register(DoctorAtHome)
class DoctorAtHomeAdmin(admin.ModelAdmin):
    list_display = ('id', 'doctor', 'patient',)
    list_display_links = ('id', 'doctor', 'patient',)


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')
    list_display_links = ('id', 'first_name', 'last_name')
