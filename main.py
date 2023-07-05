import time

def countdown(t):
    while t > 0:
        print(t)
        t -= 1
        time.sleep(1)
    print("the time has expired.. ")

print("Enter a number to start the coutdown: ")
seconds = input()

while not seconds.isdigit():
    print("The number you entered is not an integer. Please enter the exact number: ")
    seconds = input()

seconds = int(seconds)
countdown(seconds)