import copy
from operator import attrgetter

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


class Node(object):
    def __init__(self, state, g):
        self.state = copy.deepcopy(state)
        self.g = g
        self.h = heuristic(state)
        self.f = (self.g + self.h)


def a_star(init_state):
    open = []
    close = []
    g = 0
    open.append(Node(init_state, g))
    # for state in generate_states(init_state):
    #     open.append(Node(state, 1))

    # for x in open:
    #     print "g =", x.g, "h =", x.h, "f =", x.f

    count = 0
    while open:
        current = min(open, key=attrgetter('f'))
        #current = copy.deepcopy(Node(val.state, val.g))

        if current.state == GOAL_STATE:
            print "FOUND"
            break
        else:
            print "Current f =", current.f
            print_state(current.state)

        open.remove(min(open, key=attrgetter('f')))
        close.append(current)
        #        g = g + 1

        for neighbour in generate_states(current.state):
            node = Node(neighbour, current.g + 1)
            if node in close:
                print "IN CLOSE"
                pass

            if node not in open:
                open.append(node)
                print "appended f =", node.f
                print_state(node.state)

        if count == 2:
            break;
        count += 1

a = [1, 2, 3]
b = [4, 5, 6]
x = [[2,8,3], [1,0,4], [7,6,5]]
def main():
    print "\nInitial State is:"
    print_state(INIT_STATE)
    a_star(INIT_STATE)
    #print heuristic(x )


if __name__ == '__main__':
    main()
