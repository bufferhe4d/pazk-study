from sage.all import *
import sys
import time

p = next_prime(2**256)
F_p = FiniteField(p)

def gen_instance(n, yes=True):
    # A, B are two nxn matrices with random elements in F_p
    A = Matrix([[F_p.random_element() for i in range(n)] for j in range(n)])
    B = Matrix([[F_p.random_element() for i in range(n)] for j in range(n)])

    C = A*B
    
    if yes: # return a YES instance
        return (A, B, C)
    else: # change a random element in C and return a NO instance
        i, j = randrange(n), randrange(n)
        C[i,j] = F_p.random_element()
        return (A, B, C)


def frievalds(n, A, B, C):
    r = F_p.random_element() # sample r in F_p
    x = [1] # r^0 = 1
    for i in range(n-1): # generate (r^0, r^1, ..., r^{n-1})
        x.append(x[i]*r)
    x = vector(x) # convert x list to a vector

    y = C*x 
    z = A*(B*x)

    # We are checking if C*x = A*(B*x)
    return y == z

def run_bench(n, k, yes=True):
    print("Running Benchmarks for the {} instances...".format("YES" if yes else "NO"))
    
    naive_score = 0
    frievalds_score = 0

    for i in range(k):
        instance = gen_instance(n, yes)
        
        start = time.time()
        result = instance[0]*instance[1] == instance[2]
        end = time.time()
        naive_score += (end - start)

        start = time.time()
        result = frievalds(n, instance[0], instance[1], instance[2])
        end = time.time()
        frievalds_score += (end - start)

    #inst_type = yes ? "YES" : "NO"
    print("{} instance benchmark resutls over {} runs:".format("YES" if yes else "NO",  k))
    print("Naive average running time(s):", naive_score/k)
    print("Frievalds average running time(s):", frievalds_score/k, "\n")



if __name__ == '__main__':

    if len(sys.argv) == 2:
        n = int(sys.argv[1])

        # generate a YES instance
        instance = gen_instance(n)
        print("Checking a YES instance:", frievalds(n, instance[0], instance[1], instance[2]))

        # generate a NO instance
        instance = gen_instance(n, False)
        print("Checking a NO instance:", frievalds(n, instance[0], instance[1], instance[2]))
    elif len(sys.argv) == 3:
        n = int(sys.argv[1])
        k = int(sys.argv[2])
        run_bench(n, k)
        run_bench(n, k, False)
    else:
        print("usage: sage frievalds.py n k")
        print(" n: dimension of the instance matrices")
        print(" k: [OPTIONAL] number of runs for the benchmark results")
