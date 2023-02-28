import numpy as np
import math
import sys
import os
import random
import matplotlib.pyplot as plt
def Func(x): #The function we are integrating over
	return ((19*x**5)+(5*x**2)+(6*x**3)-x)
def Trapezoid(a,b): #The trapezoidal approximation of the integral
  return ((b-a)/2)*(Func(a)+Func(b))
def Gauss(n,i): #The Gaussian approximation of the integral. I'm using the Chebyshev's 2nd approximation
  return ((np.pi/(n+1))*pow(math.sin(i*np.pi/(n+1)),2)*(Func((math.cos((i/n+1)*np.pi))))*((math.sqrt(1-(math.cos((i/n+1)*np.pi))))))
def Divide(min, max, intervals): #Divide the intergrating space into usable boundaries
   assert intervals != 0
   interval_size = ((max - min) / intervals)
   result = []
   start = min
   end = min + interval_size
   while True:
      result.append([start, end])
      start = round(start + interval_size, 3)
      end = round(end + interval_size, 3)
      if len(result) == intervals:
         break
   return result
def Monte(n,vol,i,x): #The monte carlo simple integral approximation, as well as the variance
  I = 0
  MC = 0
  if i <=n:
    I = I+(vol/n)*(Func(x))
    MC = MC + Func(x)
    x= random.uniform(-1, 1)
    i = i+1
  return I, MC
#main function
if __name__ == "__main__":
  #default values, since this is taking the Chebyshev's 2nd approximation, the interval of intergation is fixed at [-1, 1]
  n = 1000
  a = -1
  b = 1
  i = 1
  x = random.uniform(-1, 1)
  # read the user-provided seed from the command line (if there)
	#figure out if you have to have -- flags before - flags or not
  if '-Nsample' in sys.argv:
	  p = sys.argv.index('-Nsample')
	  n = int(sys.argv[p+1])
  if '-h' in sys.argv or '--help' in sys.argv:
    print ("To change the number of sub-intervals: %s [-Nsample] number " % sys.argv[0])
    print
    sys.exit(1)  
  Test1 = 0
  Test2 = 0
  inter = Divide(a, b, n)
  Test3, varMC = Monte(n,10/3,i,x) #Use the monte carlo method on the function
  varMC = varMC*(10/3)*(1/math.sqrt(n)) #Calculate the variance of the Monte Carlo method
  if i <= n:   #Append the calculated area and combining it into a holder
    Test1 = Test1 + Trapezoid(inter[i-1][0],inter[i-1][1])
    Test2 = Test2 + Gauss(n,i)
    i = i+1
  Test1 = abs(Test1) #Output the values as the area
  Test2 = abs(Test2)
  E1 = (10/3) - abs(Test1) #Calculate the difference between the three approximation with the real value
  E2 = (10/3) - abs(Test2)
  print("The value of the three approximations (in order : Trapezoidal, Gaussian, and Monte Carlo) are : ", Test1, Test2, Test3)
  print("The error of the three approximations are (Trapezoidal, Gaussian, and the variance of the Monte Carlo) : ", E1, E2, varMC)
