#define a function
def func1():
   print ("I am learning Python function")
   print ("still in func1")
   
func1()

def square(x):
  	return x*x
print(square(4))

def multiply(x,y=0):
	print("value of x=",x)
	print("value of y=",y)
    
	return x*y
  
print(multiply(y=2,x=4))