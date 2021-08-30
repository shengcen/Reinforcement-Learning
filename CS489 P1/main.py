
### Policy Evaluation
theta = 0.001
v = [[0 for i in range(6)] for j in range(6)]

for i in range(6):
    for j in range(6):
        v[i][j] = 0
delta = 1
iteration = 0
while (delta >= theta):
    delta = 0
    for i in range(6):
        for j in range(6):
            upx = i - 1
            upy = j
            downx = i + 1
            downy = j
            leftx = i
            lefty = j - 1
            rightx = i
            righty = j + 1
            if (i == 0):
                upx = i
            if (i == 5):
                downx = i
            if (j == 0):
                lefty = j
            if (j == 5):
                righty = j
            if (not((i==0 and j==1) or (i==5 and j==5))):
                oldv=v[i][j]
                v[i][j] = 1/4*(-1+v[upx][upy])+1/4*(-1+v[downx][downy])+1/4*(-1+v[leftx][lefty])+1/4*(-1+v[rightx][righty])
                delta = max(delta, abs(oldv-v[i][j]))
    iteration += 1

for i in range(6):
    print(v[i])
print("Total Iteration: "+str(iteration))


### Policy Iteration
# Initialize the policy for all non-terminated states to be "up"
# grid_policy[0]---up probabilistic matrix
# grid_policy[1]---down probabilistic matrix
# grid_policy[2]---left probabilistic matrix
# grid_policy[3]---right probabilistic matrix
grid_policy = [[[0 for i in range(6)] for j in range(6)] for direction in range(4)]

# Initialize the policy to be "random"" for all non-terminated states
for i in range(6):
    for j in range(6):
        if (not ((i == 0 and j == 1) or (i == 5 and j == 5))):
            grid_policy[0][i][j] = 0.25
            grid_policy[1][i][j] = 0.25
            grid_policy[2][i][j] = 0.25
            grid_policy[3][i][j] = 0.25

for i in range(6):
    for j in range(6):
        v[i][j] = 0

improvement_count = 0
delta = 1

policy_stable = False

while not policy_stable:
    delta = 1
    while (delta >= theta):
        delta = 0
        for i in range(6):
            for j in range(6):
                upx = i - 1
                upy = j
                downx = i + 1
                downy = j
                leftx = i
                lefty = j - 1
                rightx = i
                righty = j + 1
                if (i == 0):
                    upx = i
                if (i == 5):
                    downx = i
                if (j == 0):
                    lefty = j
                if (j == 5):
                    righty = j
                if (not((i==0 and j==1) or (i==5 and j==5))):
                    oldv=v[i][j]
                    v[i][j] = grid_policy[0][i][j]*(-1+0.9*v[upx][upy])+grid_policy[1][i][j]*(-1+0.9*v[downx][downy])+grid_policy[2][i][j]*(-1+0.9*v[leftx][lefty])+grid_policy[3][i][j]*(-1+0.9*v[rightx][righty])
                    delta = max(delta, abs(oldv-v[i][j]))

    # Update policy
    improvement_count += 1
    policy_stable = True
    for i in range(6):
        for j in range(6):
            if (not ((i == 0 and j == 1) or (i == 5 and j == 5))):
                old_action_up = grid_policy[0][i][j]
                old_action_down = grid_policy[1][i][j]
                old_action_left = grid_policy[2][i][j]
                old_action_right = grid_policy[3][i][j]
                upx = i-1
                upy = j
                downx = i+1
                downy = j
                leftx = i
                lefty = j-1
                rightx = i
                righty = j+1
                if (i == 0):
                    upx = i
                if (i == 5):
                    downx = i
                if (j == 0):
                    lefty = j
                if (j == 5):
                    righty = j
                max_policy_gain = max(-1+0.9*v[upx][upy], -1+0.9*v[downx][downy], -1+0.9*v[leftx][lefty], -1+0.9*v[rightx][righty])
                tie = 0
                if (-1+0.9*v[upx][upy] == max_policy_gain): tie += 1
                if (-1 + 0.9*v[downx][downy] == max_policy_gain): tie += 1
                if (-1 + 0.9*v[leftx][lefty] == max_policy_gain): tie += 1
                if (-1 + 0.9*v[rightx][righty] == max_policy_gain): tie += 1


                if (-1+0.9*v[upx][upy] == max_policy_gain):
                    grid_policy[0][i][j] = 1/tie
                else:
                    grid_policy[0][i][j] = 0

                if (-1 + 0.9*v[downx][downy] == max_policy_gain):
                    grid_policy[1][i][j] = 1/tie
                else:
                    grid_policy[1][i][j] = 0
                if (-1 + 0.9*v[leftx][lefty] == max_policy_gain):
                    grid_policy[2][i][j] = 1/tie
                else:
                    grid_policy[2][i][j] = 0
                if (-1 + 0.9*v[rightx][righty] == max_policy_gain):
                    grid_policy[3][i][j] = 1/tie
                else:
                    grid_policy[3][i][j] = 0

                if ((old_action_up != grid_policy[0][i][j]) or (old_action_down != grid_policy[1][i][j]) or (old_action_left != grid_policy[2][i][j]) or (old_action_right != grid_policy[3][i][j])):
                    policy_stable = False

print("Up probabilistic matrix: ")
for i in range(6):
    print(grid_policy[0][i])

print("Down probabilistic matrix: ")
for i in range(6):
    print(grid_policy[1][i])

print("Left probabilistic matrix: ")
for i in range(6):
    print(grid_policy[2][i])

print("Right probabilistic matrix: ")
for i in range(6):
    print(grid_policy[3][i])

print("Value matrix: ")
for i in range(6):
    print(v[i])

print("Improvement Count: ")
print(improvement_count)


### Value Iteration
v = [[0 for i in range(6)] for j in range(6)]
iteration = 0
delta = 1
while (delta >= theta):
    delta = 0
    for i in range(6):
        for j in range(6):
            upx = i - 1
            upy = j
            downx = i + 1
            downy = j
            leftx = i
            lefty = j - 1
            rightx = i
            righty = j + 1
            if (i == 0):
                upx = i
            if (i == 5):
                downx = i
            if (j == 0):
                lefty = j
            if (j == 5):
                righty = j
            if (not((i==0 and j==1) or (i==5 and j==5))):
                oldv=v[i][j]
                v[i][j] = max(-1+0.9*v[upx][upy], -1+0.9*v[downx][downy], -1+0.9*v[leftx][lefty], -1+0.9*v[rightx][righty])
                delta = max(delta, abs(oldv-v[i][j]))
    iteration += 1

grid_policy = [[[0 for i in range(6)] for j in range(6)] for direction in range(4)]
for i in range(6):
    for j in range(6):
        if (not ((i == 0 and j == 1) or (i == 5 and j == 5))):
            upx = i - 1
            upy = j
            downx = i + 1
            downy = j
            leftx = i
            lefty = j - 1
            rightx = i
            righty = j + 1
            if (i == 0):
                upx = i
            if (i == 5):
                downx = i
            if (j == 0):
                lefty = j
            if (j == 5):
                righty = j
            max_policy_gain = max(-1 + 0.9 * v[upx][upy], -1 + 0.9 * v[downx][downy], -1 + 0.9 * v[leftx][lefty],
                                  -1 + 0.9 * v[rightx][righty])
            tie = 0
            if (-1 + 0.9 * v[upx][upy] == max_policy_gain): tie += 1
            if (-1 + 0.9 * v[downx][downy] == max_policy_gain): tie += 1
            if (-1 + 0.9 * v[leftx][lefty] == max_policy_gain): tie += 1
            if (-1 + 0.9 * v[rightx][righty] == max_policy_gain): tie += 1

            if (-1 + 0.9 * v[upx][upy] == max_policy_gain):
                grid_policy[0][i][j] = 1 / tie
            else:
                grid_policy[0][i][j] = 0

            if (-1 + 0.9 * v[downx][downy] == max_policy_gain):
                grid_policy[1][i][j] = 1 / tie
            else:
                grid_policy[1][i][j] = 0
            if (-1 + 0.9 * v[leftx][lefty] == max_policy_gain):
                grid_policy[2][i][j] = 1 / tie
            else:
                grid_policy[2][i][j] = 0
            if (-1 + 0.9 * v[rightx][righty] == max_policy_gain):
                grid_policy[3][i][j] = 1 / tie
            else:
                grid_policy[3][i][j] = 0

print("Value matrix: ")
for i in range(6):
    print(v[i])

print("Up probabilistic matrix: ")
for i in range(6):
    print(grid_policy[0][i])

print("Down probabilistic matrix: ")
for i in range(6):
    print(grid_policy[1][i])

print("Left probabilistic matrix: ")
for i in range(6):
    print(grid_policy[2][i])

print("Right probabilistic matrix: ")
for i in range(6):
    print(grid_policy[3][i])

print("Iteration to get optimal state value: ")
print(iteration)







