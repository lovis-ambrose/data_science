import multiprocessing

def calculate_square(numbers):
    for n in numbers:
        print("Square of {} is {}".format(n, n*n))
        
def calculate_cube(numbers):
    for i in numbers:
        print("Cube of {} is {}".format(i, i*i*i))
        
if __name__ == "__main__":
    arr = [2,3,8,9]
    p1 = multiprocessing.Process(target=calculate_square, args=(arr,))
    p2 = multiprocessing.Process(target=calculate_cube, args=(arr,))  # Add a comma after args=(arr,)
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    print("Done!!!!!")
