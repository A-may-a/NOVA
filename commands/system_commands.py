from datetime import datetime

def tell_time():
    return datetime.now().strftime("%I:%M %p")

def tell_date():
    return datetime.now().strftime("%d %B %Y")

def tell_day():
    return datetime.now().strftime("%A")