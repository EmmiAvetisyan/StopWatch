import time
def start_stopwATCH():
    start_time = time.time()
    input("Stopwatch stard. Press enter to stop ")
    end_time = time.time()
    varjnakan_time = end_time - start_time
    print(varjnakan_time)
    
while True:
    print("\nOptions:")
    print("1.Start StopWatch")
    print("2.Exit")
    
    choice = input("Enter you choice (1 or 2): ")
    
    if choice == "1":    
        start_stopwATCH()
    elif choice == "2":
        print("Exiting the task management system. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please enter 1 or 2")