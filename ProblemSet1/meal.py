def main():
    time_input = input("What time is it? ")
    time_compared = convert(time_input)
    if time_compared >= "420" and time_compared <= "480":
        print("Breakfast time!")
    elif time_compared >= "720" and time_compared <= "780":
        print("Lunch time!")
    elif time_compared >= "1080" and time_compared <= "1140":
        print("Dinner time!")


def convert(time):
    (hours, separator, minutes) = time.split()
    return int(hours) * 60 + int(minutes)
