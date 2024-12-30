from typing import List, Tuple, Optional

class ColoredHanoi:
    def __init__(self, n: int, disks: List[Tuple[int, str]]):
        self.n = n
        self.disks = disks
        self.moves = []
        # Initialize the rods
        self.rods = {
            'A': disks[:],  # Source rod
            'B': [],        # Auxiliary rod
            'C': []         # Target rod
        }

    def is_valid_move(self, source: str, target: str) -> bool:
        """
        Check if moving top disk from source to target is valid
        """
        if not self.rods[source]:
            return False
            
        if not self.rods[target]:
            return True
            
        # Get the disks to compare
        source_disk = self.rods[source][-1]
        target_disk = self.rods[target][-1]
        
        # Check size constraint
        if source_disk[0] > target_disk[0]:
            return False
            
        # Check color constraint
        if source_disk[1] == target_disk[1]:
            return False
            
        return True

    def move_disk(self, source: str, target: str) -> None:
        """
        Move a disk from source rod to target rod
        """
        if self.is_valid_move(source, target):
            disk = self.rods[source].pop()
            self.rods[target].append(disk)
            self.moves.append((len(self.moves) + 1, source, target))

    def solve(self) -> Optional[List[Tuple[int, str, str]]]:
        """
        Main function to solve the puzzle
        """
        def hanoi(n: int, source: str, auxiliary: str, target: str):
            if n == 0:
                return
                
            # Try moving n-1 disks to auxiliary rod
            hanoi(n-1, source, target, auxiliary)
            
            # Try moving nth disk to target
            if self.is_valid_move(source, target):
                self.move_disk(source, target)
            else:
                # If we can't make a valid move, the puzzle is impossible
                return False
                
            # Move remaining disks from auxiliary to target
            hanoi(n-1, auxiliary, source, target)
            
        # Try to solve the puzzle
        if hanoi(self.n, 'A', 'B', 'C') is False:
            return -1
            
        return self.moves

def solve_colored_hanoi(n: int, disks: List[Tuple[int, str]]) -> List[Tuple[int, str, str]]:
    """
    Solve the colored Hanoi puzzle
    """
    hanoi = ColoredHanoi(n, disks)
    result = hanoi.solve()
    return result