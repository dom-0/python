#!/usr/bin/env python3

import math

def isitprime(x):
  for y in range(2, int(math.sqrt(x)) + 1):
    if (x % y == 0):
      return (False)
  return(True)

primes = []
num = input("Enter the number till which you need primes: ")
num = int(num.rstrip())

for i in range(1, num+1):
  if isitprime(i):
    primes.append(i)
  else:
    continue

print (primes)
