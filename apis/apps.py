from django.apps import AppConfig
from datetime import datetime, timedelta
import time, threading

class ApisConfig(AppConfig):
    name = 'apis'
    def ready(self):
        from .models import Token
        WAIT_SECONDS = 60

        def delete_expired():
            # Deleting expired unallocated tokens
            Token.objects.filter(updated_at__lt=datetime.now()-timedelta(minutes=5), user__isnull=True).delete()

            # releasing expired allocated tokens after 1 minute of no use
            Token.objects.filter(updated_at__lt=datetime.now()-timedelta(minutes=1), user__isnull=False).update(status='AVAILABLE', user=None)

            threading.Timer(WAIT_SECONDS, delete_expired).start()

        delete_expired()
