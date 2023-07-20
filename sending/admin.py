from django.contrib import admin

from sending.models import Message, Sending, TrySending

admin.site.register(Message)


@admin.register(Sending)
class SendingAdmin(admin.ModelAdmin):

    list_display = ('user', 'get_customer', 'message', 'created_at', 'updated_at',
                'interval', 'status_sending', 'start_sending_date', 'start_sending_time')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(TrySending)
class SendingAdmin(admin.ModelAdmin):
    list_display = ('sending', 'last_attempt', 'status_attempt', 'answer_server')
    readonly_fields = ('sending', 'last_attempt', 'status_attempt', 'answer_server')

