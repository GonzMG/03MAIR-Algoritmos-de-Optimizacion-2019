from time import time

# To use this method, copy the method to your file
# and type on the function definition @measure_time
def measure_time(f):
    def wrapper(*args, **kwargs):
        start = time()
        result = f(*args, **kwargs)
        t = time() - start
        print("Execution time: " + str(t))
        return result
    return wrapper