'''
A very hungry worm reaches a tree and eats the leaves in the following sequence:

    DAY 1: The worm eats 1 leaf
    DAY 2: TWICE( DAY 1)= 2 leaves
    DAY 3: TWICE( DAY 2)= 4 leaves
    DAY 4: TWICE( DAY 3)= 8 leaves 
    and so on…..(up to 30 days)

The above eating sequence continues for 30 days and all the leaves finish on the 30th day. On which day did the worm finish exactly half of the total number of leaves?
'''



from collections import defaultdict

leaves_eaten_dict = defaultdict(list)
total_leaves_eaten = 0

def eat_leaves(day, leaves_eaten):
    day += 1 
    if leaves_eaten == 0:
        leaves_eaten += 1 
    else:
        leaves_eaten *= 2
    
    leaves_eaten_dict[day] = leaves_eaten
    global total_leaves_eaten
    total_leaves_eaten += leaves_eaten
    if day == 30:
        return
    else:
        eat_leaves(day, leaves_eaten)
        
        
eat_leaves(0,0)

for key,value in leaves_eaten_dict.items():
    if value == (round(total_leaves_eaten/2)):
        print('Day the worm finished exactly half of the total number of leaves:')
        print('Day: ' + str(key))
