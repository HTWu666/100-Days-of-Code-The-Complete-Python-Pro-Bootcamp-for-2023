#Prime Checker

import math

def isPrime1(number):
  is_Prime = True
  for i in range (2, number):
    if number % i == 0:
        is_Prime = False
  if is_Prime:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")
    
def isPrime2(number):
  is_Prime = True
  if number % 2 == 0:
    is_Prime = False
  else:
    for i in range(3, number, 2):
      if number % i == 0:
        is_Prime = False
  if is_Prime:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")
 

def isPrime3(number):
  is_Prime = True
  root = math.floor(math.sqrt(number))
  if number % 2 == 0:
    is_Prime = False
  else:
    for i in range (3, root):
      if number % i == 0:
        is_Prime = False
  if is_Prime:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")

n = int(input("Check this number: "))
isPrime1(number=n)
isPrime2(number=n)
isPrime3(number=n)
    
