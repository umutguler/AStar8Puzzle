import Queue as Q
import copy

# The Goal State
GOAL_STATE = [
    [1, 2, 3],
    [8, 0, 4],
    [7, 6, 5]]


# class State is the class that holds the state as a 2D list and its values
class State:
    def __init__(self, state, g = 0, parent = None):
        self.state = state
        self.g = g
        self.h = self._heuristic()
        self.f = self.g + self.h
        self.parent = parent
        self.goal = GOAL_STATE

    # the heuristic function is the sum of the Manhattan distance for every tile in the wrong position
    # when you compare to the goal state
    def _heuristic(self):
        h = 0
        for rows in xrange(3):
            for cols in xrange(3):
                if self.state[rows][cols] == 0:
                    continue
                elif self.state[rows][cols] != GOAL_STATE[rows][cols]:
                    y, x = self._get_pos(GOAL_STATE[rows][cols])
                    dist = abs(y - rows) + abs(x - cols)
                    h += dist
        return h

    # getter for g
    def get_g(self):
        return self.g

    # gets the position of a value in a 2D list and returns its y, x coordinate as a tuple
    def _get_pos(self, v):
        for i, x in enumerate(self.state):
            if v in x:
                return i, x.index(v)

    # returns all possible states from a given state as a list of 2D lists
    def valid_state(self):
        y, x = self._get_pos(0)  # assigns y and x of 0
        valid_states = []  # initialize list

        # checks above
        if y > 0:
            temp_state = copy.deepcopy(self.state)  # copies state to a temp state
            temp_state[y][x] = temp_state[y - 1][x]  # sets 0 to above tile
            temp_state[y - 1][x] = 0  # sets above tile to 0
            new_state = State(temp_state, self.g + 1, self.state)  # sets new state
            valid_states.append(new_state)  # adds new state to list

        # checks below
        if y < 2:
            temp_state = copy.deepcopy(self.state)  # copies state to a temp state
            temp_state[y][x] = temp_state[y + 1][x]  # sets 0 to below tile
            temp_state[y + 1][x] = 0  # sets below tile to 0
            new_state = State(temp_state, self.g + 1, self.state)  # sets new state
            valid_states.append(new_state)  # adds new state to list

        # checks left
        if x > 0:
            temp_state = copy.deepcopy(self.state)  # copies state to a temp state
            temp_state[y][x] = temp_state[y][x - 1]  # sets 0 to left tile
            temp_state[y][x - 1] = 0  # sets left tile to 0
            new_state = State(temp_state, self.g + 1, self.state)  # sets new state
            valid_states.append(new_state)  # adds new state to list

        # checks right
        if x < 2:
            temp_state = copy.deepcopy(self.state)  # copies state to a temp state
            temp_state[y][x] = temp_state[y][x + 1]  # sets 0 to right tile
            temp_state[y][x + 1] = 0  # sets right tile to 0
            new_state = State(temp_state, self.g + 1, self.state)  # sets new state
            valid_states.append(new_state)  # adds new state to list

        return valid_states

    # function prints state nicely as 2d array with its g, h and f values or not
    def print_state(self, stats = None):
        if stats:
            print "g =", self.g, "h =", self.h, "f =", self.f
        for rows in xrange(3):
            for cols in xrange(3):
                print self.state[rows][cols],
                if cols == 2:
                    print
        print

    # gets parents to rebuild path
    def get_parents(self, parent):
        if parent is None:
            return

        print "g =", parent.g, "h =", parent.h, "f =", parent.f
        for rows in xrange(3):
            for cols in xrange(3):
                print parent.state[rows][cols],
                if cols == 2:
                    print
        print
        self.get_parents(parent.parent)

    def __cmp__(self, other):
        if other is None:
            return 1
        return self.f > other.f


# AStar class contains the actual algorith,
class AStar:
    def __init__(self, init_state = None, goal_state = None):
        self.init_state = init_state
        self.goal_state = goal_state
        self.parent = None

    # A* algorithm
    def search(self):
        open_set = []  # open set of all neighbours but not evaluated
        open_g = []  # open set g score
        open_set.append(self.init_state)  # appends initial state to open set
        open_g.append(0)  # appends initial g score
        close = []  # closed set contains all visited and evaluated states
        temp = Q.PriorityQueue()  # temporary priority queue
        temp.put(State(self.init_state, 0))  # appends State() to priority queue

        # while temp is not empty
        while temp:
            current = temp.get()  # current is equal to the priority queue's returned value

            # if current state is equal to the goal state
            if current.state == self.goal_state:
                print "FOUND, where g =", current.g  # print out stats
                print "Path:\n\n"  # print the path reversed
                current.get_parents(current.parent)  # get parent function prints the path
                break  # end the loop

            close.append(current.state)  # append the current state to the closed set
            neighbours = State(current.state, current.g, current)  # neighbours are returned possible values of current

            # for loop iterates through neighbours
            for state in neighbours.valid_state():
                # if state is in close, skip
                if state.state in close:
                    continue
                # otherwise if state is not in open set
                # add state tp the temp priority queue
                elif state.state not in open_set:
                    temp.put(State(state.state, current.g + 1, current))


# 13 Initial State to test from the provided PDF document
# Each is harder/takes more moves
INIT_STATE = [
    [
        [2, 8, 3],
        [1, 6, 4],
        [7, 0, 5]],
    [
        [2, 1, 6],
        [4, 0, 8],
        [7, 5, 3]],
    [
        [5, 7, 2],
        [0, 8, 6],
        [4, 1, 3]],
    [
        [0, 6, 5],
        [4, 1, 7],
        [3, 2, 8]],
    [
        [0, 6, 5],
        [4, 1, 8],
        [3, 7, 2]],
    [
        [6, 5, 7],
        [4, 1, 0],
        [3, 2, 8]],
    [
        [6, 5, 7],
        [4, 0, 1],
        [3, 2, 8]],
    [
        [6, 5, 7],
        [4, 2, 1],
        [3, 0, 8]],
    [
        [5, 6, 7],
        [0, 4, 8],
        [3, 2, 1]],
    [
        [6, 5, 7],
        [4, 2, 1],
        [3, 8, 0]],
    [
        [0, 5, 7],
        [6, 4, 1],
        [3, 2, 8]],
    [
        [5, 6, 7],
        [4, 0, 8],
        [3, 2, 1]],
    [
        [2, 0, 4],
        [1, 3, 5],
        [7, 8, 6]],
]


def main():
    count = 1
    while True:
        for state in INIT_STATE:
            print "Initial state:", count
            State(state).print_state(False)
            count += 1

        i = input("Type 0 = Quit\nEnter which initial state to test, 1 to 13: ")

        if 0 < i <= 13:
            AStar(INIT_STATE[i - 1], GOAL_STATE).search()
            raw_input("Press enter to continue . . .")
            count = 0

        if i == 0:
            break


if __name__ == '__main__':
    main()
