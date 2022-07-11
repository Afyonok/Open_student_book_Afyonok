#игра загадай число
import numpy as np

number = np.random.randint(1,101) #загадываем число от 1 до 100

count = 0
while True:
    count += 1
    predict_number = int(input('попробуй угадать число от 1 до 100  6'))
    
    if predict_number > number:
        print('загаданное число меньше')
        
    elif predict_number < number:
         print('загаданное число больше')
         
    else:
         print(f'вы угадали, это число = {number}, за {count} попыток')
         break