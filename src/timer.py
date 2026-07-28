import time

def start(minutes):

    seconds = minutes * 60

    while seconds > 0:

        print(f"Remaining: {seconds}s", end="\r")

        time.sleep(1)

        seconds -= 1

    print("\nSession completed!")
