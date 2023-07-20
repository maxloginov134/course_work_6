from datetime import datetime, date, time

from django.core.mail import send_mail

from sending.models import Sending, TrySending
from sending.utils import install_nex_date
from config import settings


def sending_mail():
    query_sending = Sending.objects.exclude(status_sending=Sending.COMPLITED) \
        .filter(start_sending_date=date.today()) \
        .filter(start_sending_time__lte=time(*list(map(int, datetime.now().time().strftime("%H:%M:%S").split(':')))))

    for sending in query_sending:
        email_list = [x.email for x in sending.customer.all()]
        sending.status_sending = Sending.ACTIVATED
        sending.save()
        try:
            result = send_mail(
                subject=sending.message.theme,
                message=sending.message.content,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=email_list,
                fail_silently=False
            )
            if result:
                TrySending.objects.create(sending=sending,
                                          last_attempt=datetime.now(),
                                          status_attempt='success',
                                          answer_server='ok')
                sending.start_sending_date = install_nex_date(sending)
                sending.save()
        except Exception as error:
            TrySending.objects.create(sending=sending,
                                      last_attempt=datetime.now(),
                                      status_attempt='failure',
                                      answer_server=error)
