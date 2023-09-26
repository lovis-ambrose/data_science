import time
import threading
# program to demostrate multithreading. It is faster compared to the normal execution
def calulate_square(numbers):
    print("Square of numbers")
    for i in numbers:
        # put a waiting time, memory is idle
        time.sleep(0.2)
        print("Square of {} is {}".format(i, i*i))
        
def calculate_cube(numbers):
    print("Cube of Numbers")
    for n in numbers:
        time.sleep(0.2)
        print("Cube of {} is {} \n".format(n, n*n*n))
        
        
# define array
arr = [2,3,8,9]
t = time.time()
# threads
t1 = threading.Thread(target= calulate_square, args=(arr,))
t2 = threading.Thread(target=calculate_cube, args=(arr,))

# start the threads
t1.start()
t2.start()

# join the tasks and execute them in parallel
# ie calculate square then go and calculate cube while waiting for the sleep time on calculate_square to end
t1.join()
t2.join()

# shoow the time taken to execute
print("done in: ", time.time()-t)
