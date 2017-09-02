from heapq import heappush, heappop, heapify
from operator import attrgetter

import copy

import sys

GOAL_STATE = [
    [1, 2, 3],
    [8, 0, 4],
    [7, 6, 5]]

# This state should take 5 moves to complete
INIT_STATE = [
    [2, 8, 3],
    [1, 6, 4],
    [7, 0, 5]]


class State:
    def __init__(self, state, g = 0, parent = None):
        self.state = state
        self.g = g
        self.h = self._heuristic()
        self.f = self.g + self.h
        self.parent = parent
        self.goal = GOAL_STATE

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

    def _get_pos(self, v):
        for i, x in enumerate(self.state):
            if v in x:
                return i, x.index(v)

    def valid_state(self):
        y, x = self._get_pos(0)
        valid_states = []

        # check above
        if y > 0:
            temp_state = copy.deepcopy(self.state)
            temp_state[y][x] = temp_state[y - 1][x]
            temp_state[y - 1][x] = 0
            new_state = State(temp_state, self.g + 1, self.state)
            valid_states.append(new_state)
            del temp_state[:][:]

        # check below
        if y < 2:
            temp_state = copy.deepcopy(self.state)
            temp_state[y][x] = temp_state[y + 1][x]
            temp_state[y + 1][x] = 0
            new_state = State(temp_state, self.g + 1, self.state)
            valid_states.append(new_state)
            del temp_state[:][:]

        # check left
        if x > 0:
            temp_state = copy.deepcopy(self.state)
            temp_state[y][x] = temp_state[y][x - 1]
            temp_state[y][x - 1] = 0
            new_state = State(temp_state, self.g + 1, self.state)
            valid_states.append(new_state)
            del temp_state[:][:]

        # check right
        if x < 2:
            temp_state = copy.deepcopy(self.state)
            temp_state[y][x] = temp_state[y][x + 1]
            temp_state[y][x + 1] = 0
            new_state = State(temp_state, self.g + 1, self.state)
            valid_states.append(new_state)
            del temp_state[:][:]

        return valid_states

    def print_state(self):
        print "g =", self.g, "h =", self.h, "f =", self.f
        for rows in xrange(3):
            for cols in xrange(3):
                print self.state[rows][cols],
                if cols == 2:
                    print
        print


class AStar:
    def __init__(self, init_state = None, goal_state = None):
        self.init_state = init_state
        self.goal_state = goal_state

    def _rebuild_path(self):
        pass

    def search(self):
        open = []
        open.append(self.init_state)
        close = []
        g = 0
        min_f = sys.maxint

        while open:
            print "SEARCHING F"
            for state in open:
                temp = State(state, g, state)
                temp.print_state()
                if temp.f < min_f:
                    print "LESS"
                    min_f = temp.f
                    current = temp

            if current.state == self.goal_state:
                print "FOUND"
                break
            if g == 1:
                break
            open.remove(current.state)
            close.append(current.state)

            print "CURRENT"
            current.print_state()
            neighbours = State(current.state, g, current.state)

            for state in neighbours.valid_state():
                # state.print_state()

                if state.state in close:
                    print "in closed"
                    continue

                # t_g = g + 1
                # if t_g >= g:
                #     print t_g
                #     continue

                if state.state not in open:
                    print "appending open"
                    open.append(state.state)

            g += 1


tstate = [
    [2, 0, 3],
    [1, 8, 4],
    [7, 6, 5]]


def main():
    AStar(INIT_STATE, GOAL_STATE).search()
    # State(tstate).print_state()


class PriorityQueue:
    def __init__(self):
        self.pq = []

    def add(self, item):
        heappush(self.pq, item)

    def poll(self):
        return heappop(self.pq)

    def peek(self):
        return self.pq[0]

    def remove(self, item):
        value = self.pq.remove(item)
        heapify(self.pq)
        return value is not None

    def __len__(self):
        return len(self.pq)


if __name__ == '__main__':
    main()
