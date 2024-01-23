#What is Python?
'''Python is a high-level,dynamically-typed,interpreted,oop(object-oriented-programming) language created by Guido Van Rossum in the year 1989 and was released to the public in 1991.The Python programming language 
was created at the National Netherlands Research Institute using the C programming language,which was developed by Dennis Ritchie in 1972,shared a close interaction with hardware,was used to build operating systems 
and device drivers and influenced many modern programming languages" syntax.Python is used in the fields of Data Science,Machine Learning,Web Development,back-end development,automation tasks,cybersecurity and robotics.
The Python programming language has 35 reserved keywords and 68 built-in functions.Python libraries are coded in C or Rust which are both low-level programming languages.'''
#What is a variable?
'''A variable is a symbolic name which references an object.Variables are stored in the RAM(Random Access Memory),where they have a name,content and address.A Python interpreter would interpret all these attributes of a 
variable stored in memory.Variables can be mutable or immutable based on the type of object they are referencing.Variables are used to store different types of data,for example:str,int,float,list,tuple,set,dict,range,bytes,bytearray,frozenset,None,bool.
In Python,there are 3 types of variables,global,local and nonlocal.A global variable is a variable which is defined outside a function  or inside a function.These types of variables can be accessed and manipulated inside and 
outside functions.A local variable is a variable which is defined inside a function and belongs to the function's scope.These types of variables can never be used outside a function.If you attempt to use a local variable 
outside a function,you will get a NameError,saying that variable wasn't defined.A nonlocal variable is a variable which is defined in Python decorators.In order to create a variable in Python,you first write the Python 
identifier followed by the equal sign and then the object the variable is referencing.'''
#What is a for loop?
'''A for loop is a loop where the loop variable iterates over a subscriptable sequence for example:str,list,tuple,set,dict.If you attempt to loop over a non-iterable sequence,you would get a TypeError,saying that 
object wasn't subscriptable.For loops print text vertically,repeats a block of code a specific amount of times and has 2 loop control statements,break and continue.The break statement stops the execution of the 
for loop immediately,whereas the continue statement stops the current iteration of the for loop and skips it.Both of these Python keywords are used  in if statements.'''
#What is an if statment?
'''An if statement is a conditional statement which checks if a particular condition has been met or not before the execution path.If statements are used for decision-making in programming.If statements,ulitlise 
comparison operators,to compare 2 values,identity operators,to check if 2 objects are in the same memory location,membership operators,to check if a variable is present in a specific iterable container and logical 
operators,to add more functionality to if statements.If a condition was not met,an else or elif statement would be written,handling that condition.'''
#What is a tuple?
'''A tuple is a data structure which is immutable and ordered.'''
#What is a dictionary?
'''A dictionary is a data structure which stores data in key-value pairs.'''
#What is a while loop?
'''A while loop is a loop which repeats a block of code as long as the logical condition is True.'''
#What is type castings?
'''The conversion from one data type to another without any data loss.'''
#What is a Python identifier?
'''A Python identifier is a name for a variable,function,class or a Python module.
In order to create a Python identifier it must satisfy these conditions:
1.Cannot exceed 79 characters 
2.Cannot start with any numerical values 
3.Should contain both upper and lowecase letters 
4.You cannot use Python keywords as identifiers 
5.You cannot use special characters,except an underscore character 

A Python identifier which starts with an underscore character is a private identifier.Whereas a Python identifier which starts and ends with 2 underscore characters is a special language defined identifier.'''
#What is a list?
'''A list is a data structure or a collections data which stores multiple values,items or elements of a similar data type in one variable.
list functions:
list.append()-Appends an object to the end of the list 
list.insert()-Takes 2 positional arguments,index and object.Appends an object at the specified index.
list.reverse()-Reverses a list 
list.sort()-Sorts a list  in ascending order
list.count()-Counts the occurences of a value in a list 
list.index()-Returns the index of a value present in a list 
list.pop()-Deletes an object at the specified index. 
del list[]-Deletes an object at the specified index. 
list.extend()-Adds values existing from another iterable container to the end of the list.'''
#What are the 4 concepts of OOP:
'''OOP Concepts:
1.Data Abstraction 
2.Encapsulation
3.Inheritance 
4.polymorphism '''
#What is the lambda function?
'''The lambda function is a small anonymous function that takes an unlimited amount of arguments but can only have one expression.'''
#What is JSON?
'''Json is a data format that stands  for JavaScript Object Notation.It is heavily used for data exchange  in web applications.'''
from colorama import Fore 
import time 
import sys   
import os 
import random
three_digit_binary_number=['1','0','1','1','0','0','1','0','1','0','0','1',]      
#Creating a function that takes in a subscriptable sequence and prints it horizontially  
def loop_over(sequence,color):
    for text in sequence:
        sys.stdout.flush()
        sys.stdout.write(f'{color}{text}')
    else:
        pass    
for n in range(40):
    three_digit_binary_number.append('1')
    three_digit_binary_number.append('0')        
dot_frame_1='.'
dot_frame_2='     .'
dot_frame_3='               .'
dot_frame_4='                           .'
dot_frame_5='                                         .'
dot_frame_6='                                                          .'
dot_frame_7='                                                                        .'
dot_frame_8='                                                                                          .'
dot_frame_9='                                                                                                                     . '
dot_frame_10='                                                                                                                                                       .'
dot_frame_11='                                                                                                                                                          . '
dot_frame_12='                                                                                                                                                                                           .'
print(f'{dot_frame_1}',end='\r')
time.sleep(0.1)
print(f'{dot_frame_2}',end='\r')
time.sleep(0.1)
print(f'{dot_frame_3}',end='\r')
time.sleep(0.1)
print(f'{dot_frame_4}',end='\r')
time.sleep(0.1)
print(f'{dot_frame_5}',end='\r')
time.sleep(0.1)
print(f'{dot_frame_6}',end='\r')
time.sleep(0.1)
print(f'{dot_frame_7}',end='\r')
time.sleep(0.1)
print(f'{dot_frame_8}',end='\r')
time.sleep(0.1)
print(f'{dot_frame_9}',end='\r')
time.sleep(0.1)
print(f'{dot_frame_10}',end='\r')
time.sleep(0.1)
print(f'{dot_frame_11}',end='\r')
time.sleep(0.1)
print(f'{dot_frame_12}')
if dot_frame_12:
    time.sleep(1)
    os.system('cls')
    time.sleep(1)
    while True:
        random.shuffle(three_digit_binary_number)
        loop_over(sequence=f'{" ".join(three_digit_binary_number)}\n',color=Fore.GREEN)