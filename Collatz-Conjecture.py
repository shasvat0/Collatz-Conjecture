import time, math
print("Enter a number:")
number = int(input(''))

def collatz(number):
  if number % 2 == 0:
    result = (number//2)
    print(number//2)
    return number // 2
  else:
    result = (number*3) + 1
    print((number*3) + 1)
    return (number*3) + 1
  
  

while 1 != number:
  number = collatz(number)
  
time.sleep(math.pow(2,10))