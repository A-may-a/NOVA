import random

def who_are_you():
    return "I am Nova, your intelligent virtual assistant."

def how_are_you():
    return "I am functioning perfectly."

def tell_joke():

    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs.",
        "A programmer's wife tells him get milk and if they have eggs get a dozen. He returns with twelve cartons of milk.",
        "There are 10 types of people. Those who understand binary and those who do not."
    ]

    return random.choice(jokes)