import schedule

from sms import send_sms

schedule.every(1).hour.do(send_sms)

while True:
    schedule.run_pending()
