import time

while True:    
    
    user_input = input("Enter number of seconds to begin the timer: ")
    
    if not user_input.isdigit(): # Check if the input is a valid number
        
        print("Please enter a valid number.")
        
        continue
    
    seconds = int(user_input)
    
    for i in range(seconds, 0, -1):
        
        print(i)
        
        time.sleep(1)
        
    print("Time's up!")
    
    break
