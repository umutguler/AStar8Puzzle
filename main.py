import copy

GOAL_STATE = [
    [1, 2, 3],
    [8, 0, 4],
    [7, 6, 5]]

# This state should take 5 moves to complete
INIT_STATE = [
    [2, 8, 3],
    [1, 6, 4],
    [7, 0, 5]]

g = 0
h = 0


def find_empty_pos(state):
    x = y = - 1

    for rows in state:
        y += 1
        for cols in rows:
            if x == 3:
                x = 0
            x += 1
            if cols == 0:
                break
    return x, y


# checks up, down, left, right of empty position
# swaps the empty to a neighbouring value
# returns the valid states as a list
def generate_states(state):
    x, y = find_empty_pos(state)
    valid_states = []

    # check above
    if y > 0:
        temp_state = copy.deepcopy(state)
        temp_state[y][x] = temp_state[y - 1][x]
        temp_state[y - 1][x] = 0
        valid_states.append(temp_state)

    # check below
    if y < 2:
        temp_state = copy.deepcopy(state)
        temp_state[y][x] = temp_state[y + 1][x]
        temp_state[y + 1][x] = 0
        valid_states.append(temp_state)

    # check left
    if x > 0:
        temp_state = copy.deepcopy(state)
        temp_state[y][x] = temp_state[y][x - 1]
        temp_state[y][x - 1] = 0
        valid_states.append(temp_state)

    # check right
    if x < 2:
        temp_state = copy.deepcopy(state)
        temp_state[y][x] = temp_state[y][x + 1]
        temp_state[y][x + 1] = 0
        valid_states.append(temp_state)

    return valid_states


def print_state(state):
    for rows in xrange(3):
        for cols in xrange(3):
            print state[rows][cols],
            if cols == 2:
                print
    print


def heuristic(state):
    h = 0
    for rows in xrange(3):
        for cols in xrange(3):
            if state[rows][cols] != GOAL_STATE[rows][cols]:
                h = h + 1
    return h


class Node:
    def __init__(self, state, g, h):
        self.state = copy.deepcopy(state)
        self.g = g
        self.h = h
        self.f = (g + h)



def a_star(init_state):
    open = []
    open.append(Node(init_state, 0, 0))

    while open:
        pass


def main():
    print "\nInitial State is:"
    print_state(INIT_STATE)

    a_star(INIT_STATE)




if __name__ == '__main__':
    main()
