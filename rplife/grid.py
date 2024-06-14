import collections

class LifeGrid:
    def __init__(self, pattern):
        self.pattern = pattern

    def evolve(self):
        neighbors =( (-1, -1), 
                    (-1, 0), 
                    (-1, 1), 
                    (0, -1), 
                    (0, 1), 
                    (1, -1), 
                    (1, 0), 
                    (1, 1) )
        num_neighbors = collections.defaultdict(int)
        for row, col in self.pattern.alive_cells:
            for drow, dcol in neighbors:
                num_neighbors[(row+drow, col+dcol)] += 1

        stay_alive = {
            cell for cell, num in num_neighbors.items() 
            if num in {2,3} 
            } & self.pattern.alive_cells
        come_alive = {cell for cell, num in num_neighbors.items() 
                      if num == 3
                      } - self.pattern.alive_cells
        self.pattern.alive_cells = stay_alive | come_alive

    def as_string(self, bbox):
        pass
    def __str__(self):
        return (
            f"{self.pattern.name}:\n"
            f"alive cells -> {sorted(self.pattern.alive_cells)}"
        )
        