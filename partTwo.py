import math  

def main():
    A = int(input("Enter A: "))
    B = int(input("Enter B: "))
    c = pythag (A, B)
    print (c) 

def pythag(A,B):
   c=math.sqrt ((A**2)+(B**2))
   return c


main()
