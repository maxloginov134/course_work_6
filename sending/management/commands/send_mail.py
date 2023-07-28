from django.core.management import BaseCommand

from sending.cron import sending_mail


class Command(BaseCommand):
    def handle(self, *args, **options):
        sending_mail()
