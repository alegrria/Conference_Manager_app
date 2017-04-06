Conference Track Management

----------------------------
Desigh Explanation
----------------------------
The structure of the program is simple: extract text from a given file, 
map talk titles to their durations, use first fit algorithm to create sessions,
add timing to sessions, form tracks and print them.

I chose the first fit algorithm for creating sessions, because creating sessions 
is a bin packing problem, which is NP-hard, and optimal solutions require compicated
algorithms. The first fit algorithm is a greedy algorithm and gives a non-optimal 
but acceptable solution, totally suitable for the case of making a schedule for
a conference.

Running Instructions
---------------------------
for Mac:
The program can be run in Terminal by running main.py and input file with python.
Input file should be in the same directory as main.py. Run the program with 
"python main.py test_input.txt" (or any other input file name)