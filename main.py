from heapq import heappush, heappop, heapify
from operator import attrgetter

import copy

import sys

GOAL_STATE = [
    [1, 2, 3],
    [8, 0, 4],
    [7, 6, 5]]


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

        # check below
        if y < 2:
            temp_state = copy.deepcopy(self.state)
            temp_state[y][x] = temp_state[y + 1][x]
            temp_state[y + 1][x] = 0
            new_state = State(temp_state, self.g + 1, self.state)
            valid_states.append(new_state)

        # check left
        if x > 0:
            temp_state = copy.deepcopy(self.state)
            temp_state[y][x] = temp_state[y][x - 1]
            temp_state[y][x - 1] = 0
            new_state = State(temp_state, self.g + 1, self.state)
            valid_states.append(new_state)

        # check right
        if x < 2:
            temp_state = copy.deepcopy(self.state)
            temp_state[y][x] = temp_state[y][x + 1]
            temp_state[y][x + 1] = 0
            new_state = State(temp_state, self.g + 1, self.state)
            valid_states.append(new_state)

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

        while open:
            temp = []
            for state in open:
                temp.append(State(state, g, state))
            current = min(temp, key = attrgetter('f'))

            if current.state == self.goal_state:
                print "FOUND g =", g
                break

            open.remove(current.state)
            close.append(current.state)
            neighbours = State(current.state, g, current.state)

            for state in neighbours.valid_state():
                if state.state in close:
                    continue

                if state.state not in open:
                    open.append(state.state)

            g += 1


tstate = [
    [2, 0, 3],
    [1, 8, 4],
    [7, 6, 5]]

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
    for state in INIT_STATE:
        AStar(state, GOAL_STATE).search()

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
