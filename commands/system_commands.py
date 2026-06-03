
from datetime import datetime

def tell_time():

    now = datetime.now()

    print(now.strftime("%I:%M %p"))

    return now.strftime("%I:%M %p")