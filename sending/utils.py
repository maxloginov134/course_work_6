from datetime import timedelta

from sending.models import Sending


def install_nex_date(sending: Sending):
    if sending.interval == sending.ONE_A_DAY:
        sending.start_sending_date += timedelta(days=1)
    elif sending.interval == sending.ONE_A_WEEK:
        sending.start_sending_date += timedelta(days=7)
    else:
        sending.start_sending_date += timedelta(days=30)

    return sending.start_sending_date
