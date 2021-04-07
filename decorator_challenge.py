import time

start_time = time.time()


def speed_calc_decorator(function):
    def wrapper_function():
        first = start_time
        function()
        second = time.time()
        print(f"{function.__name__} run speed: {second - first}")
    return wrapper_function



@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


fast_function()
slow_function()