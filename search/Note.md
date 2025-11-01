# Search Problems

A **search problem** typically involves the following components:

- **An agent:** The thinking part of the program.
- **Initial state:** The starting point of the problem.
- **Actions:** The possible moves or steps the agent can take.
- **Transition model:** Describes the result of performing an action in a given state.
- **Goal test:** Determines whether a given state is a goal state.
- **Path cost function:** Assigns a numeric cost to each path.

In a search process, data is often stored in a **node**, a data structure that contains the following information:

- The **state**.
- Its **parent node**, from which the current node was generated.
- The **action** applied to the parent’s state to reach the current node.
- The **path cost** from the initial state to this node.

All of this information enables **backtracking** during the search.

---

# Uninformed Search

An **uninformed search** strategy uses no problem-specific knowledge to guide its search; it relies solely on the problem definition.

## Search Algorithms

### Breadth-First Search (BFS)

- Uses a **queue** data structure (FIFO).
- Guaranteed to find the **optimal solution** if all step costs are equal.

### Depth-First Search (DFS)

- Uses a **stack** data structure (LIFO).
- Often the fastest in some scenarios.
- However, the solution found may **not be optimal**.

---

# Informed Search

An **informed search** strategy uses problem-specific knowledge (heuristics) to find solutions more efficiently.

## Greedy Best-First Search

A search algorithm that expands the node **closest to the goal**, as estimated by a heuristic function **h(n)**.

## A* Search

A search algorithm that expands the node with the **lowest value** of:

```
f(n) = g(n) + h(n)
```

Where:
- **g(n):** The cost to reach node *n*.
- **h(n):** The estimated cost from *n* to the goal.

In other words, A* considers both how far it has come (**g(n)**) and how far it is estimated to go (**h(n)**).

### A* is optimal if:

- **h(n)** is *admissible* (never overestimates the true cost), and
- **h(n)** is *consistent* (for every node *n* and successor *n’* with step cost *c*,
  `h(n) <= h(n') + c`).

---

# Adversarial Search Problems

These are search problems that involve competition between two or more agents.

## Minimax Algorithm

Used in adversarial environments (like games) to minimize the possible loss in a worst-case scenario.

## Alpha-Beta Pruning

An optimization technique for the Minimax algorithm that eliminates branches that cannot influence the final decision, improving efficiency.

---

# Projects

### 1. Degrees

Implemented the `shortest_path` function to return the shortest path between two people — from a **source** (person ID) to a **target** (person ID).

### 2. Tic-Tac-Toe

Implemented an **intelligent agent** that plays the game optimally against an adversary using adversarial search techniques.
