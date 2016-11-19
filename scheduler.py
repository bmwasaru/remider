import schedule

from sms import vote

schedule.every(1).hour.do(vote)

while True:
    schedule.run_pending()
