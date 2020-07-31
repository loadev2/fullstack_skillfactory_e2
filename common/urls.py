from django.urls import path
from common.views import ListMessage,  add_email

app_name = 'common'
urlpatterns = [
    path('list/', ListMessage.as_view(), name='list'),
    path('', add_email, name="send_email")
]