## Exercise #1 <br>
#Cube Number Test... Print out all cubed numbers up to the total value 1000. Meaning that if the cubed number is over 1000 break the loop

cubes = []
for number in range(1, 11):
    cube = number**3
    cubes.append(cube)

for cube in cubes:
    print(cube)

## Exercise #2 <br>
#Get first prime numbers up to 100 # this part I looked up the code to better understand how it is written.
# 
# Python3 program to display Prime numbers till N
  
#function to check if a given number is prime
def isPrime(n):
  #since 0 and 1 is not prime return false.
  if(n==1 or n==0):
    return False
    
  #Run a loop from 2 to n-1/ 
  for i in range(2,n):
    #if the number is divisible by i, then n is not a prime number.
    if(n%i==0):
      return False
    
  #otherwise, n is prime number.
  return True
  
  
  
# Driver code
N = 100
#check for every number from 1 to N
for i in range(1,N+1):
  #check if current number is prime
  if(isPrime(i)):
    print(i,end=" ")




#Exercise 3
#Take in a users input for their age, if they are younger than 18 print kids, if they're 18 to 65 print adults, else print seniors

age = 15
if age < 18:
    print("kids")
elif age < 65:
    print("Adult")
else:
    print("senior")
