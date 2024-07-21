#problem1
x= int(input("enter a nonnegative nb: "))
if(x<0):
    print("negative number!")
elif(x==0):
    print(1)
else:
    output=1
    for i in range(1,x+1):
        output*=i
        
    print(output)

#problem2

l1="The wheels on the bus go"
l2="round and round,"
l3="all through the town."
print(l1,3*l2,l1,l2,l3)

#problem3

a= float(input("enter 'a'"))
b= float(input("enter'b'"))
c= float(input("enter 'c'"))
delta = b**2 -4*a*c

if delta>0:
    firstRoot = (-b+delta**0.5)/(2*a)
    secondRoot = (-b-delta**0.5)/(2*a)
    print("Roots of :",a,"x2 + ",b,"x +",c,"are:",firstRoot,"and",secondRoot)
elif delta==0:
    root=-b/(2*a)
    print("Root of :"+a+"x2 + "+b+"x +"+c+"is",root)
else:
    print("no real roots")

#problem4

n = int(input("enter a nonnegative number"))
for i in range(n-1,1,-1):
    if n%i==0:
        print(n,"is not prime")
        break
else:
    print(n,"is Prime")
#2nd part
n = int(input("enter a nonnegative number"))
i=2
while i<=(n**(1/2)):
      if n%i==0:
            print(n,"is not prime")
            break
      i+=1
else: print(n,"is Prime")

for k in range (2,int(n**(0.5))+1):
      if n%k==0:
            print(n,"is not prime")
            break
else: print(n,"is Prime")

#problem5

n = int(input("enter x:"))
countOfprimeNumbers =0
for k in range(2,n+1):
    isPrime  =True
    for i in range(2,int(k**(0.5))+1):
        if k%i==0:
            isPrime=False
            break    
    if isPrime:
        countOfprimeNumbers+=1
print("Fraction of primes less than or equal to",n,":",countOfprimeNumbers/n)
    
    
#problem6
from random import randint
s=randint(1,100)
n=1
guessCounter=0
close =False
lastGuessDifference = 0
while n :
    
    guess=int(input("give a guess:"))
    diff = abs(guess-s)
    
    if guess<1 or guess>100:
        print("OUT OF BOUNDS")
    if diff<=10 and not close:
        print("WARM!")
        close=True
        lastGuessDifference = diff
    elif diff>10 and not close:
        print("COLD!")
    elif guess==s:
        print("correct!")
        guessCounter+=1
        print("nb of guesses",guessCounter)
        n-=1
    elif close and diff<=lastGuessDifference:
        print("WARMER!")
        lastGuessDifference=diff
    elif close and diff>lastGuessDifference:
        print("COLDER!")
        lastGuessDifference=diff

    guessCounter+=1
    


    


 

    
