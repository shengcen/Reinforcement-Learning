import random

decay = 0.9

# ### MC (first visit)
avg_v = [[0 for i in range(6)] for j in range(6)]
v = [[0 for m in range(6)] for n in range(6)]
v_all = 0
visited = [[False for p in range(6)] for q in range(6)]
state_count = [[0 for x in range(6)] for y in range(6)]
my_episode=list()

ini_x=random.randint(0,5)
ini_y=random.randint(0,5)

for i in range(1000):
    while (not ((ini_x == 0 and ini_y == 1) or (ini_x == 5 and ini_y == 5))):
        my_direction=random.randint(0,3)
        if my_direction==0:
            if ini_x != 0:
                ini_x = ini_x - 1
        if my_direction == 1:
            if ini_x != 5:
                ini_x = ini_x + 1
        if my_direction == 2:
            if ini_y !=0:
                ini_y = ini_y - 1
        if my_direction == 3:
            if ini_y != 5:
                ini_y = ini_y + 1

        my_episode.append([ini_x,ini_y])

    for item in reversed(my_episode):
        if (not ((item[0] == 0 and item[1] == 1) or (item[0] == 5 and item[1] == 5))):
            v_all = -1 + decay * v_all
            v[item[0]][item[1]] = v_all
            visited[item[0]][item[1]] = True
    state_count[ini_x][ini_y] = state_count[ini_x][ini_y] +1
    for row in range(6):
        for col in range(6):
            if visited[row][col]:
                state_count[row][col] = state_count[row][col] + 1
                avg_v[row][col] = avg_v[row][col] + 1/state_count[row][col] * (v[row][col] - avg_v[row][col])

    for row in range(6):
        for col in range(6):
            v[row][col] = 0
            visited[row][col] = False
    v_all = 0
    ini_x = random.randint(0, 5)
    ini_y = random.randint(0, 5)
    my_episode = list()

for i in range(6):
    print(avg_v[i])


### MC (every visit)
avg_v = [[0 for i in range(6)] for j in range(6)]
v = [[0 for m in range(6)] for n in range(6)]
v_all = 0
state_count = [[0 for x in range(6)] for y in range(6)]
my_episode=list()

ini_x=random.randint(0,5)
ini_y=random.randint(0,5)

for i in range(1000):
    while (not ((ini_x == 0 and ini_y == 1) or (ini_x == 5 and ini_y == 5))):
        my_direction=random.randint(0,3)
        if my_direction==0:
            if ini_x != 0:
                ini_x = ini_x - 1
        if my_direction == 1:
            if ini_x != 5:
                ini_x = ini_x + 1
        if my_direction == 2:
            if ini_y !=0:
                ini_y = ini_y - 1
        if my_direction == 3:
            if ini_y != 5:
                ini_y = ini_y + 1

        my_episode.append([ini_x,ini_y])

    for item in reversed(my_episode):
        if (not ((item[0] == 0 and item[1] == 1) or (item[0] == 5 and item[1] == 5))):
            v_all = -1 + decay * v_all
            v[item[0]][item[1]] = v_all
            state_count[item[0]][item[1]] = state_count[item[0]][item[1]] + 1
            avg_v[item[0]][item[1]] = avg_v[item[0]][item[1]] + 1/state_count[item[0]][item[1]] * \
                                      (v[item[0]][item[1]] - avg_v[item[0]][item[1]])

    v_all = 0
    ini_x = random.randint(0, 5)
    ini_y = random.randint(0, 5)
    my_episode = list()

for i in range(6):
    print(avg_v[i])



### TD0

alpha = 0.01
v = [[0 for m in range(6)] for n in range(6)]

ini_x=random.randint(0,5)
ini_y=random.randint(0,5)


for i in range(1000):
    while (not ((ini_x == 0 and ini_y == 1) or (ini_x == 5 and ini_y == 5))):
        my_direction=random.randint(0,3)
        old_vx=ini_x
        old_vy=ini_y
        if my_direction==0:
            if ini_x != 0:
                ini_x = ini_x - 1
        if my_direction == 1:
            if ini_x != 5:
                ini_x = ini_x + 1
        if my_direction == 2:
            if ini_y !=0:
                ini_y = ini_y - 1
        if my_direction == 3:
            if ini_y != 5:
                ini_y = ini_y + 1

        v[old_vx][old_vy] = v[old_vx][old_vy] + alpha * (-1 + decay * v[ini_x][ini_y] - v[old_vx][old_vy])
    ini_x = random.randint(0, 5)
    ini_y = random.randint(0, 5)

for i in range(6):
    print(v[i])







