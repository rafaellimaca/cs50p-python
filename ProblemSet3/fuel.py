def turn_into_percentage(fraction):
    segments = fraction.split("/")
    dividend = int(segments[0])
    divisor = int(segments[1])
    percentage = dividend / divisor *100
    if dividend < 0 :
        raise ValueError
    return float(percentage)

def fuel_checker(percentage):
    if float(percentage) <= 1:
        return "E"
    elif float(percentage) >= 100:
        return "F"
    else:
        return percentage

def main():
    done = False
    while not done:
        fraction = (input("Enter a fraction: "))
        try:
            turn_into_percentage(fraction)
        except (ValueError, ZeroDivisionError):
            pass
        else:
            print(f"{fuel_checker(turn_into_percentage(fraction))}%")
            break

main()
