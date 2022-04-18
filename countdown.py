import time
import datetime
import os
 
# Create class that acts as a countdown
def countdown(h, m, s):
 
    total_seconds = h * 3600 + m * 60 + s

    while total_seconds > 0:
 
        # Timer represents time left on countdown
        timer = datetime.timedelta(seconds = total_seconds)

        print(timer, end="\r")
 
        time.sleep(1)

        total_seconds -= 1
 
    print("Bzzzt! The countdown is at zero seconds!")
    os.startfile("beep.wav")

while True:
  h = input("Enter the time in hours: ")
  m = input("Enter the time in minutes: ")
  s = input("Enter the time in seconds: ")
  countdown(int(h), int(m), int(s))