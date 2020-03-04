from django.contrib import admin

from api.models import Model, Ticket, Status, Comment


class TicketAdmin(admin.ModelAdmin):
    list_display = ('user', 'model', 'client_name', 'imei', 'status')
    list_filter = ('status',)


admin.site.register(Ticket, TicketAdmin)
admin.site.register(Model)
admin.site.register(Status)
admin.site.register(Comment)
