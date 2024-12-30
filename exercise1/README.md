# Colored Towers of Hanoi

This implementation solves a variation of the classic Towers of Hanoi puzzle with additional color constraints.

## Problem Description

The puzzle consists of n disks of different sizes and colors stacked on a source rod. The goal is to transfer all disks to a target rod using an auxiliary rod, following these rules:

1. Only one disk can be moved at a time
2. A larger disk cannot be placed on top of a smaller disk
3. Disks of the same color cannot be placed directly on top of each other
4. The solution must use recursion

## Implementation Details

The solution uses a class-based approach with the following components:

- `ColoredHanoi`: Main class that handles the puzzle logic
- `is_valid_move`: Validates moves based on size and color constraints
- `move_disk`: Executes valid moves between rods
- `solve`: Implements the recursive solution algorithm

## Usage

```python
from towers_of_hanoi import solve_colored_hanoi

# Example usage
n = 3
disks = [(3, "red"), (2, "blue"), (1, "red")]
result = solve_colored_hanoi(n, disks)
print(result)
```

## Running Tests

To run the tests:

```bash
python -m pytest test_towers.py
```

## Output Format

The solution returns either:

- A list of moves in the format `(move_number, source_rod, target_rod)`
- `-1` if the puzzle is impossible to solve

## Requirements

- Python 3.6+
- pytest (for running tests)
