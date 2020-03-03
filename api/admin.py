from django.contrib import admin

from .models import Models, Tickets, Status

class TicketsAdmin(admin.ModelAdmin):
    list_display = ('user', 'model', 'client_name', 'imei', 'status')
    list_filter = ('status',)

admin.site.register(Tickets, TicketsAdmin)
admin.site.register(Models)
admin.site.register(Status)
