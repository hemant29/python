#Accessing Values in Strings
var1 = "Guru99!"
var2 = "Software Testing"
print ("var1[0]:",var1[0])
print ("var2[1:5]:",var2[1:5])
#Some more examples
x = "Hello World!"
print (x[:6]) 
print (x[0:6] + "Guru99")
#Python String replace() Method
oldstring = 'I like Guru99' 
newstring = oldstring.replace('like', 'love')
print (newstring)
#Changing upper and lower case strings
string="python at guru99"
print (string.upper())
string="python at guru99.hemant am learning basic"		
print (string.capitalize())
string="PYTHON AT GURU99"
print (string.lower())
#Using "join" function for the string
print(":".join("Python"))		
#Reversing String
string="12345"		
print(''.join(reversed(string)))
#Split Strings
word="guru99 career guru99"		
print (word.split(' '))
word="guru99 career guru99"		
print (word.split('r'))
x = "Guru99"
x.replace("Guru99","Python")
print (x)
x = "Guru99"
x = x.replace("Guru99","Python")
print (x)