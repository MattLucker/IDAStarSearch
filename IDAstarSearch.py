import math
import copy
from puzzle import *
from createAlgs import alg

"""
DESC:   The heart of the project. IDAstarSearch.py is the IDA* search algorithm that calculates scramble solutions.
        Can be self run for individual scrambles or get called by solver.py for lists of scrambles.

path              current search path (acts like a stack)
node              current node (last node in current path)
g                 the cost to reach current node
f                 estimated cost of the cheapest path (root..node..goal)
h(node)           estimated cost of the cheapest path (node..goal)
cost(node, neigh) step cost function
is_goal(node)     goal test
neighbors(node)   node expanding function, expand nodes ordered by g + h(node)
ida_star(root)    return either None or a pair with the best path and its cost
"""

def neighbors(lastMove):
    possMoves = ["r","rp","r2","l","lp","l2","u","up","u2","d","dp","d2","f","fp","f2","b","bp","b2"]
    q = []
    for possMove in possMoves:
        if lastMove[0] != possMove[0]:
            q.append(possMove)
    return q


def search(path, g, bound, p):
    node = path[1:]
    p.reset()
    p.execute(node)
    f = g + p.h()
    if f > bound:
        return f
    if p.solved():
        return -1
    min = float('inf')
    for neigh in neighbors(path[-1]):
        path.append(neigh)
        t = search(path, g + 1, bound, p)
        if t == -1:
            return -1
        if t < min:
            min = t
        path.pop()
    return min


def ida_star(p):
    bound = p.h()
    path = ["x"]
    while True:
        t = search(path, 0, bound, p)
        if t == -1:
            return (path, bound)
        if t == float('inf'):
            return None, None
        bound = t


# Is called by a function in solver.py for mass solving.
def run(scramble):
    p = cube()
    p.execute(scramble)
    p.save()
    path, bound = ida_star(p)
    if path == ["x"]:
        print("No path found.")
        return None
    print(path[1:-1])
    return len(path)-1


# Use for individual scrambles and testing.
if __name__ == "__main__":
    scramble = "fp rp f rp u f rp f2 up r f u2 r u2 fp up fp rp"#alg(9)
    print("\nGiven Scramble:", scramble)
    p = cube()
    algo = p.decode(scramble)
    p.display()
    p.execute(algo)
    p.save()
    print()
    p.display()
    path, bound = ida_star(p)
    print()
    print("Scramble: ", scramble)
    if path == ["x"]:
        print("No path found.")
    else:
        solution = ""
        for p in path[1:]:
            solution += p + " "
        print("Solution: " + solution)
