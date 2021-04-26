from IDAstarSearch import run
from tqdm import tqdm
import time

"""
DESC:   Opens a list of algs found in algs.txt, solves each one, and writes the solution and runtime for each example
        in solutions.txt and times.txt respectively.
"""

def main():
    r = open("algs.txt","r")
    t = open("times.txt","w")
    s = open("solutions.txt","w")
    numoalgs = int(r.readline())
    #t.write(str(numoalgs)+"\n")
    #s.write(str(numoalgs)+"\n")
    #tqdm (range (numoalgs), desc="Loading..."):
    for i in tqdm (range (numoalgs), desc="Loading..."):
        line = r.readline()
        alg = line.split()
        startTime = time.time()
        solution = run(alg)
        totalTime = time.time()-startTime
        totalTime = round(totalTime,3)
        t.write(str(totalTime)+"\n")
        s.write(str(solution)+"\n")
    r.close
    t.close
    s.close
main()
