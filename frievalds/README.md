## Frievalds' Algorithm in Sage

Usage: 
~~~
usage: sage frievalds.py n k
 n: dimension of the instance matrices
 k: [OPTIONAL] number of runs for the benchmark results
~~~

Example: 
~~~
$ sage frievalds.py 20 100

Running Benchmarks for the YES instances...
YES instance benchmark resutls over 100 runs:
Naive average running time(s): 0.0027204036712646486
Frievalds average running time(s): 0.0011887550354003906 

Running Benchmarks for the NO instances...
NO instance benchmark resutls over 100 runs:
Naive average running time(s): 0.002684013843536377
Frievalds average running time(s): 0.0006026148796081543 
~~~
