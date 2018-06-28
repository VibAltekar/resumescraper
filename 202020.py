import schedule
import time
import os

# os.system("gem install terminal-notifier")
def job():
    print("LOOK AWAY FROM SCREEN")
    notify(title="look away bruh", subtitle = "srsly bruh", message = "forreals doe")
    os.system("say 'look away from screen'")


def notify(title, subtitle, message):
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    os.system('terminal-notifier {}'.format(' '.join([m, t, s])))

# Calling the function
notify(title    = 'A Real Notification',
       subtitle = 'with python',
       message  = 'Hello, this is me, notifying you!')

schedule.every(20).minutes.do(job)
schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

