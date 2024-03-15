import time


def slow_function():
    print('Start function')
    time.sleep(5)
    print('End function')


print('Start slow_function')
slow_function()
print('End slow_function')
