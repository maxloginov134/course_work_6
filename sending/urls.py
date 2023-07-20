from django.urls import path

from sending.views import CreateMessage, DetailMessage, ListMessages, UpdateMessage, DeleteMessage, DeleteSendingView, \
    ListSending, CreateSending, DetailSending, UpdateSendingView, DisableSendingView, ListTrySending

app_name = 'sending'

urlpatterns = [
    path('create_message/', CreateMessage.as_view(), name='create_message'),
    path('detail_message/<int:pk>/', DetailMessage.as_view(), name='detail_message'),
    path('list_message/', ListMessages.as_view(), name='list_message'),
    path('update_message/<int:pk>/', UpdateMessage.as_view(), name='update_message'),
    path('delete_message/<int:pk>/', DeleteMessage.as_view(), name='delete_message'),

    path('delete_sending/<int:pk>/', DeleteSendingView.as_view(), name='delete_sending'),
    path('list_sending/', ListSending.as_view(), name='list_sending'),
    path('create_sending/', CreateSending.as_view(), name='create_sending'),
    path('ditail_sending/<int:pk>/', DetailSending.as_view(), name='detail_sending'),
    path('update_sending/<int:pk>/', UpdateSendingView.as_view(), name='update_sending'),
    path('disable_sending/<int:pk>/', DisableSendingView.as_view(), name='disable_sending'),
    path('disable_sending/<int:pk>/', DisableSendingView.as_view(), name='disable_sending'),
    path('list_try_sending/', ListTrySending.as_view(), name='list_try_sending'),
]
