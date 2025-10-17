## Search Problems involve:

- An Agent (the thinking part of the program)
- Initial state
- Actions
- Transition model
- Goal test
- Path cost function

In a search process, data is often stored in a node, a data structure that contains the following data:

- A state
- Its parent node, through which the current node was generated
- The action that was applied to the state of the parent to get to the current node
- The path cost from the initial state to this node
  All this is to ensure backtracking.

# Uninformed search

Search strategy that uses no problem-specific knowledge.

## Search Algorithms

### Breadth First Search

- Queue data structure (FIFO)
- Guaranteed to find optimal solution.

### Depth First Search

- Stack data structure (LIFO)
- At best, this algorithm is the fastest.
- It is possible that the found solution is not optimal.

# Informed search
Search strategy that uses problem-specific knowledge to find solutions more
efficiently.

## Greedy Best-First search
Search algorithm that expands the node that is closest to the goal, as estimated
by a heuristic function h(n)

## A * Search
Search algorithm that expands node with lowest value of g(n) + h(n)
g(n) = cost to reach node
h(n) = estimated cost to goal
i.e how many exhausted to my current state(g(n)) + how far I am to the goal(h(n))
### Optimal if
- h(n) is admissible (never overestimates the true cost), and
- h(n) is consistent (for every node n and successor n` with step cost c,
h(n) <= h(n`) + c)

# Adversarial Search Problem
## Minimax Algorithm
