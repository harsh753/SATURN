# stone
''' stone vs paper --> paper
stone vs scissor --> stone'''
# paper
''' paper vs stone --> paper
paper vs scissor--> scissor'''
# scissor
''' scissor vs paper --> scissor
scissor vs stone--> stone'''

import random
import time

def game(computer,user):
    if computer=='st':
        if user=='p':
            return True

    if computer=='st':
        if user=='s':
            return False

    if computer==user:
        return None

    if computer=='p':
        if user=='st':
            return False

    if computer=='p':
        if user=='s':
            return True

    if computer=='s':
        if user=='st':
            return True

    if computer=='s':
        if user=='p':
            return False


print('compter choose from stone(st),paper(p) and scissors(s)')
number=random.randint(1,3)
if number==1:
    comp='st'
if number==2:
    comp='p'
if number==3:
    comp='s'
a=input('player choose from stone(st),paper(p) and scissors(s): ')
time.sleep(1)

d=game(comp,a)
print(f'player chooses {a} and computer chooses {comp}')
print('plss wait')
time.sleep(3)

if d==None:
    print('it is a tie')
elif d==True:
    print('player wins')
else:
    print('computer wins')

while True:
    b=input('want to continue? yes or no: ')
    print()
    if b=='yes':
        print('compter choose from stone(st),paper(p) and scissors(s)')
        number=random.randint(1,3)
        if number==1:
            comp='st'
           
        if number==2:
            comp='p'
            
        if number==3:
            comp='s'
            
        a=input('player choose from stone(st),paper(p) and scissors(s): ')
        time.sleep(1)
        d=game(comp,a)
        print(f'player chooses {a} and computer chooses {comp}')
        print('plss wait')
        time.sleep(3)
        if d==None:
            print('it is a tie')
            
        elif d==True:
            print('player wins')
            
        else:
            print('computer wins')
            
    elif b=='no':
        exit()







