# UMC201
HOME WORK


 # DATA STRUCTURE AND ALGORITHM
---------------------------------
# 1. A Python program that processes ultra-large integers. (Note that in Python, the int datatype supports ultra-large integers.
------------------------------------------------------------------------------------------------------------------------------
My task: Make the given Python program faster by:
(Optional) Optimizing the Python algorithm.
(Required) Rewriting parts of the Python implementation in C/C++, including a C/C++ data structure for ultra-large integer calculations.
Given files:
hw1.py: Do not modify this file.
count_pairs.py: Modify this file so that the hw1.py program runs faster.
A sample input file (inputs.txt)

# 2. Reimplement the dictionary (dict.c, dict.h)
------------------------
By using trie dict must be implemented as a trie and it must implement all the functions in dict_adt.h. You must not include any global variables. (You are free to #define things.) *** There is ONE exception: The given (naive) dict.c has a hard-coded limit of DICT_SIZE entries. There should be no hard-coded limit in your dictionary. The set function should return 0 only if you cannot allocate additional heap memory.

Assumptions: The key will always be a string of lowercase English letters ('a' to 'z'). The maximum key length is defined in dict_adt.h and the values (id's) are 32-bit ints.
# Link : https://en.wikipedia.org/wiki/Trie

# 3. probabilistic data structure 
---------------------------
The following is a pure Python implementation of a very cool probabilistic data structure called HyperLogLog:
we optimize the get_nearest_neighbors function in the file hll.py.
# link: https://github.com/svpcom/hyperloglog

# 4. SPLAY TREE
-------------------
A suitable data structure for the following task involving n distinct numbers.
- Step 1: The n numbers will be provided (in some random order) and should be stored in the data structure.
- Step 2: A series of m queries (m much larger than n) will be performed, where at least c.m of these queries will be for one of the numbers x provided in Step 1. (Here, 0 < c < 1 is a constant, independent of n).
The required data structure must ensure that the amortized cost of each search for x is O(1), where the hidden cone.javastant can depend on c.
My Task is experimentally convince my friend that splay trees could be an appropriate data structure
# link:https://github.com/TheAlgorithms/Java/blob/master/src/main/java/com/thealgorithms/datastructures/trees/SplayTre

--------------------------------

### Technologies Used

-Python 3.12+
-NumPy
-c/c++ , java implementation
-Matplotlib / Seaborn for visualizations

## Acknowledgements

We are extend our sincere gratitude to
## Professor C. Pandu Rangan & prof. Viraj kumar
for his support throughout the SEMESTER for providing the opportunity to explore this topic through a graded  **HOMEWORK ASSIGNMENT** in their course
