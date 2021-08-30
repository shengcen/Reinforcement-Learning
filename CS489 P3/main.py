
import random

epsilon=0.1
# epsilon =0
alpha=0.1

def next_position(mystate_row,mystate_col,action):

    if (mystate_row==2 and (mystate_col>=1 and mystate_col<=10) and action==1):
        next_row=3
        next_col=0
        reward=-100
    elif (mystate_row==3 and mystate_col==0 and action==3):
        next_row = 3
        next_col = 0
        reward = -100
    else:
        if action==0:
            next_row=mystate_row-1
            next_col=mystate_col
        if action==1:
            next_row=mystate_row+1
            next_col = mystate_col
        if action==2:
            next_col=mystate_col-1
            next_row=mystate_row
        if action==3:
            next_col = mystate_col+1
            next_row = mystate_row


        if (action==0 and mystate_row==0):
            next_row=0
        if (action==1 and mystate_row==3 and mystate_col==0):
            next_row=3
        if (action==2 and mystate_col==0):
            next_col=0
        if (action == 3 and mystate_col == 11):
            next_col = 11
        reward=-1
    return next_row,next_col,reward


Q_up=[[0 for col in range(12)] for row in range(4)]
Q_down=[[0 for col2 in range(12)] for row2 in range(4)]
Q_left=[[0 for col3 in range(12)] for row3 in range(4)]
Q_right=[[0 for col4 in range(12)] for row4 in range(4)]


def best_dir(curr_row, curr_col):
    mymax=Q_up[curr_row][curr_col]
    mybest=0
    if (Q_down[curr_row][curr_col]>mymax):
        mymax=Q_down[curr_row][curr_col]
        mybest=1
    if (Q_left[curr_row][curr_col]>mymax):
        mymax=Q_left[curr_row][curr_col]
        mybest=2
    if (Q_right[curr_row][curr_col]>mymax):
        # mymax=Q_right[curr_row][curr_col]
        mybest=3
    return mybest

def next_move(curr_row, curr_col):
    mybest=best_dir(curr_row,curr_col)
    my_rand=random.uniform(0, 1)
    if my_rand<=(epsilon/4):
        mynext=(mybest+1)%4
    elif my_rand>(epsilon/4) and my_rand<=(epsilon/2):
        mynext=(mybest+2)%4
    elif my_rand>(epsilon/2) and my_rand<=(3*epsilon/4):
        mynext=(mybest+3)%4
    else:
        mynext=mybest
    return mynext


## Sarsa
#
for i in range(1000):
    curr_row=3
    curr_col=0
    my_act=next_move(curr_row,curr_col)
    while not(curr_row==3 and curr_col==11):
        next_row,next_col,reward=next_position(curr_row,curr_col,my_act)
        next_act=next_move(next_row, next_col)

        if (my_act==0):
            if (next_act==0):
                Q_up[curr_row][curr_col]=Q_up[curr_row][curr_col]+alpha*(reward+Q_up[next_row][next_col]-Q_up[curr_row][curr_col])
            elif (next_act==1):
                Q_up[curr_row][curr_col] = Q_up[curr_row][curr_col] + alpha * (
                            reward + Q_down[next_row][next_col] - Q_up[curr_row][curr_col])
            elif (next_act==2):
                Q_up[curr_row][curr_col] = Q_up[curr_row][curr_col] + alpha * (
                            reward + Q_left[next_row][next_col] - Q_up[curr_row][curr_col])
            else:
                Q_up[curr_row][curr_col] = Q_up[curr_row][curr_col] + alpha * (
                            reward + Q_right[next_row][next_col] - Q_up[curr_row][curr_col])
        elif (my_act==1):
            if (next_act==0):
                Q_down[curr_row][curr_col]=Q_down[curr_row][curr_col]+alpha*(reward+Q_up[next_row][next_col]-Q_down[curr_row][curr_col])
            elif (next_act==1):
                Q_down[curr_row][curr_col] = Q_down[curr_row][curr_col] + alpha * (
                            reward + Q_down[next_row][next_col] - Q_down[curr_row][curr_col])
            elif (next_act==2):
                Q_down[curr_row][curr_col] = Q_down[curr_row][curr_col] + alpha * (
                            reward + Q_left[next_row][next_col] - Q_down[curr_row][curr_col])
            else:
                Q_down[curr_row][curr_col] = Q_down[curr_row][curr_col] + alpha * (
                            reward + Q_right[next_row][next_col] - Q_down[curr_row][curr_col])
        elif (my_act==2):
            if (next_act==0):
                Q_left[curr_row][curr_col]=Q_left[curr_row][curr_col]+alpha*(reward+Q_up[next_row][next_col]-Q_left[curr_row][curr_col])
            elif (next_act==1):
                Q_left[curr_row][curr_col] = Q_left[curr_row][curr_col] + alpha * (
                            reward + Q_down[next_row][next_col] - Q_left[curr_row][curr_col])
            elif (next_act==2):
                Q_left[curr_row][curr_col] = Q_left[curr_row][curr_col] + alpha * (
                            reward + Q_left[next_row][next_col] - Q_left[curr_row][curr_col])
            else:
                Q_left[curr_row][curr_col] = Q_left[curr_row][curr_col] + alpha * (
                            reward + Q_right[next_row][next_col] - Q_left[curr_row][curr_col])
        else:
            if (next_act==0):
                Q_right[curr_row][curr_col]=Q_right[curr_row][curr_col]+alpha*(reward+Q_up[next_row][next_col]-Q_right[curr_row][curr_col])
            elif (next_act==1):
                Q_right[curr_row][curr_col] = Q_right[curr_row][curr_col] + alpha * (
                            reward + Q_down[next_row][next_col] - Q_right[curr_row][curr_col])
            elif (next_act==2):
                Q_right[curr_row][curr_col] = Q_right[curr_row][curr_col] + alpha * (
                            reward + Q_left[next_row][next_col] - Q_right[curr_row][curr_col])
            else:
                Q_right[curr_row][curr_col] = Q_right[curr_row][curr_col] + alpha * (
                            reward + Q_right[next_row][next_col] - Q_right[curr_row][curr_col])
        curr_row=next_row
        curr_col=next_col
        my_act=next_act

print("Q_up:")
for i in range(4):
    print(Q_up[i])
print("Q_down:")
for i in range(4):
    print(Q_down[i])
print("Q_left:")
for i in range(4):
    print(Q_left[i])
print("Q_right:")
for i in range(4):
    print(Q_right[i])



## q-learning

Q_up=[[0 for col in range(12)] for row in range(4)]
Q_down=[[0 for col2 in range(12)] for row2 in range(4)]
Q_left=[[0 for col3 in range(12)] for row3 in range(4)]
Q_right=[[0 for col4 in range(12)] for row4 in range(4)]

for i in range(1000):
    curr_row=3
    curr_col=0

    while not(curr_row==3 and curr_col==11):
        my_act = next_move(curr_row, curr_col)
        next_row,next_col,reward=next_position(curr_row,curr_col,my_act)
        next_act=best_dir(next_row,next_col)

        if (my_act==0):
            if (next_act==0):
                Q_up[curr_row][curr_col]=Q_up[curr_row][curr_col]+alpha*(reward+Q_up[next_row][next_col]-Q_up[curr_row][curr_col])
            elif (next_act==1):
                Q_up[curr_row][curr_col] = Q_up[curr_row][curr_col] + alpha * (
                            reward + Q_down[next_row][next_col] - Q_up[curr_row][curr_col])
            elif (next_act==2):
                Q_up[curr_row][curr_col] = Q_up[curr_row][curr_col] + alpha * (
                            reward + Q_left[next_row][next_col] - Q_up[curr_row][curr_col])
            else:
                Q_up[curr_row][curr_col] = Q_up[curr_row][curr_col] + alpha * (
                            reward + Q_right[next_row][next_col] - Q_up[curr_row][curr_col])
        elif (my_act==1):
            if (next_act==0):
                Q_down[curr_row][curr_col]=Q_down[curr_row][curr_col]+alpha*(reward+Q_up[next_row][next_col]-Q_down[curr_row][curr_col])
            elif (next_act==1):
                Q_down[curr_row][curr_col] = Q_down[curr_row][curr_col] + alpha * (
                            reward + Q_down[next_row][next_col] - Q_down[curr_row][curr_col])
            elif (next_act==2):
                Q_down[curr_row][curr_col] = Q_down[curr_row][curr_col] + alpha * (
                            reward + Q_left[next_row][next_col] - Q_down[curr_row][curr_col])
            else:
                Q_down[curr_row][curr_col] = Q_down[curr_row][curr_col] + alpha * (
                            reward + Q_right[next_row][next_col] - Q_down[curr_row][curr_col])
        elif (my_act==2):
            if (next_act==0):
                Q_left[curr_row][curr_col]=Q_left[curr_row][curr_col]+alpha*(reward+Q_up[next_row][next_col]-Q_left[curr_row][curr_col])
            elif (next_act==1):
                Q_left[curr_row][curr_col] = Q_left[curr_row][curr_col] + alpha * (
                            reward + Q_down[next_row][next_col] - Q_left[curr_row][curr_col])
            elif (next_act==2):
                Q_left[curr_row][curr_col] = Q_left[curr_row][curr_col] + alpha * (
                            reward + Q_left[next_row][next_col] - Q_left[curr_row][curr_col])
            else:
                Q_left[curr_row][curr_col] = Q_left[curr_row][curr_col] + alpha * (
                            reward + Q_right[next_row][next_col] - Q_left[curr_row][curr_col])
        else:
            if (next_act==0):
                Q_right[curr_row][curr_col]=Q_right[curr_row][curr_col]+alpha*(reward+Q_up[next_row][next_col]-Q_right[curr_row][curr_col])
            elif (next_act==1):
                Q_right[curr_row][curr_col] = Q_right[curr_row][curr_col] + alpha * (
                            reward + Q_down[next_row][next_col] - Q_right[curr_row][curr_col])
            elif (next_act==2):
                Q_right[curr_row][curr_col] = Q_right[curr_row][curr_col] + alpha * (
                            reward + Q_left[next_row][next_col] - Q_right[curr_row][curr_col])
            else:
                Q_right[curr_row][curr_col] = Q_right[curr_row][curr_col] + alpha * (
                            reward + Q_right[next_row][next_col] - Q_right[curr_row][curr_col])
        curr_row=next_row
        curr_col=next_col

print("Q_up:")
for i in range(4):
    print(Q_up[i])
print("Q_down:")
for i in range(4):
    print(Q_down[i])
print("Q_left:")
for i in range(4):
    print(Q_left[i])
print("Q_right:")
for i in range(4):
    print(Q_right[i])
