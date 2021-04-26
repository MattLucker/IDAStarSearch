"""
DESC:   Creates algs.txt which contains a list of algorithms varying by inputs.

IN:     create_algs.py 'number of algs' 'length of algs'
RET:    list of algorithms of specified lengths
Note:   Can do multiple inputs such as 5 5 10 10: 5 algs of len 5 followed by 10
        algs of len 10. Number of inputs must be even.
"""
import sys
from random import choice

def alg(length):
    movesets = [["r","rp","r2"],["l","lp","l2"],["u","up","u2"],["d","dp","d2"],["f","fp","f2"],["b","bp","b2"]]
    alg = ""
    move = ""
    for j in range(length):
        moveset = choice(movesets)
        while move in moveset:
            moveset = choice(movesets)
        move = choice(moveset)
        alg += move + " "
    alg += '\n'
    return alg

def build(num, length, f):
    num = int(num)
    length = int(length)
    for i in range(num): # Ensures no turn for the same side is repeated (e.g. alg: r rp is redundant)
        f.write(alg(length))

def main():
    if len(sys.argv)%2 != 1 or len(sys.argv) < 3:
        return 0

    f = open("algs.txt", "w")
    total = 0
    for i in range(1,len(sys.argv),2):
        total += int(sys.argv[i])
    f.write(str(total)+'\n')
    for i in range(1,len(sys.argv),2):
        build(sys.argv[i],sys.argv[i+1],f)
    f.close()

main()
