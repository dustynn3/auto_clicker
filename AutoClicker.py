import mouse
import time


def main():
    print("Loop started. Ctrl + C at any time to stop program.")
    counter = 0
    time.sleep(3)
    while True:
        mouse.click('left')
        print("Click!")
        counter += 1
        print("Total clicks:", counter )
        time.sleep(.01)
        if counter == 150:
            print("Counter reached", counter, "clicks, stopping.")
            break
            
            

try:
    main()
except KeyboardInterrupt:
    pass
    print("Program stopped.")

    
    


