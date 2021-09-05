import os
import time


# print(dir(os))
# os.rename('./myfile.txt', './myfile2.txt')
# os.unlink('./myfile2.txt')

print(dir(time))
# print(time.__doc__)

time1 = time.time()

numbers = range(1, 5000000)
for number in numbers:
    square = number ** 2


time2 = time.time()
difference = time2 - time1
print(f"time taken = {difference}")
