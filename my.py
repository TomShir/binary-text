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
