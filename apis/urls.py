from django.urls import path
from apis import views
from datetime import datetime, timedelta
import time, threading

urlpatterns = [
    path('generate/', views.generate_token, name='generate_token'),
    path('assign/', views.assign_token, name='assign_token'),
    path('unblock/<str:token>/', views.unblock_token, name='unblock_token'),
    path('delete/<str:token>/', views.delete_token, name='delete_token'),
    path('keep-alive/<str:token>/', views.keep_alive_token, name='keep_alive_token'),
]

from .models import Token
WAIT_SECONDS = 60

def delete_expired():
    # Deleting expired unallocated tokens
    Token.objects.filter(updated_at__lt=datetime.now()-timedelta(minutes=5), user__isnull=True).delete()

    # releasing expired allocated tokens after 1 minute of no use
    Token.objects.filter(updated_at__lt=datetime.now()-timedelta(minutes=1), user__isnull=False).update(status='AVAILABLE', user=None)

    threading.Timer(WAIT_SECONDS, delete_expired).start()

delete_expired()
