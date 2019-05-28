max_value = 100


def find_state(pos):
    pos[0] = 0
    pos[1] = 0
    pos[2] = 1
    pos[3] = 1
    pos[4] = 1
    pos[5] = 1
    pos[6] = 1
    pos[7] = 0
    pos[8] = 0

    # find winner for other positions
    for i in range(9, max_value + 1):
        if not (pos[i - 2]) or not (pos[i - 3]) or not (pos[i - 5]):
            pos[i] = 1
        else:
            pos[i] = 0


# driver function
N = int(input("Pls enter number of stones : "))
pos = [0] * (max_value + 1)

find_state(pos)

if pos[N] == 1:
    print("Alice is winner")
else:
    print("Bob is winner")
