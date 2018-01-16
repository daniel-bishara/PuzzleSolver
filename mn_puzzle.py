from puzzle import Puzzle


class MNPuzzle(Puzzle):
    """
    An nxm puzzle, like the 15-puzzle, which may be solved, unsolved,
    or even unsolvable.
    """

    def __init__(self, from_grid, to_grid):
        """
        MNPuzzle in state from_grid, working towards
        state to_grid

        @param MNPuzzle self: this MNPuzzle
        @param tuple[tuple[str]] from_grid: current configuration
        @param tuple[tuple[str]] to_grid: solution configuration
        @rtype: None
        """
        # represent grid symbols with letters or numerals
        # represent the empty space with a "*"
        assert len(from_grid) > 0
        assert all([len(r) == len(from_grid[0]) for r in from_grid])
        assert all([len(r) == len(to_grid[0]) for r in to_grid])
        self.n, self.m = len(from_grid), len(from_grid[0])
        self.from_grid, self.to_grid = from_grid, to_grid

    # TODO
    # implement __eq__ and __str__
    # __repr__ is up to you

    def __eq__(self,other):
        return self.from_grid==other.from_grid and self.to_grid==other.to_grid
    def __str__(self):
        string_representation=""
        for row in self.from_grid:
            for element in row:
                string_representation+=(str(element)+" ")
            string_representation=string_representation.strip()
            string_representation+="\n"

        return string_representation.strip()
    def extensions(self):
        for a in range(self.n):
            for b in range(self.m):
                if self.from_grid[a][b]=="*":
                    x,y=b,a
        extension_list=[]
        if x>0:
            new_tuple=list(self.from_grid)
            new_tuple[y]=list(new_tuple[y])#
            new_tuple[y][x],new_tuple[y][x-1]=self.from_grid[y][x-1],self.from_grid[y][x]
            new_tuple[y]=tuple(new_tuple[y])#
            extension_list.append(MNPuzzle(tuple(new_tuple),self.to_grid))
        if x<self.m-1:
            new_tuple=list(self.from_grid)
            new_tuple[y]=list(new_tuple[y])#
            new_tuple[y][x],new_tuple[y][x+1]=self.from_grid[y][x+1],self.from_grid[y][x]
            new_tuple[y]=tuple(new_tuple[y])#
            extension_list.append(MNPuzzle(tuple(new_tuple),self.to_grid))
        if y>0:
            new_tuple=list(self.from_grid)
            new_tuple[y],new_tuple[y-1]=list(new_tuple[y]),list(new_tuple[y-1])#
            new_tuple[y][x],new_tuple[y-1][x]=self.from_grid[y-1][x],self.from_grid[y][x]
            new_tuple[y],new_tuple[y-1]=tuple(new_tuple[y]),tuple(new_tuple[y-1])
            extension_list.append(MNPuzzle(tuple(new_tuple),self.to_grid))
        if y<self.n-1:
            new_tuple=list(self.from_grid)
            new_tuple[y],new_tuple[y-1]=list(new_tuple[y]),list(new_tuple[y-1])#
            new_tuple[y][x],new_tuple[y+1][x]=self.from_grid[y+1][x],self.from_grid[y][x]
            new_tuple[y],new_tuple[y-1]=tuple(new_tuple[y]),tuple(new_tuple[y-1])
            extension_list.append(MNPuzzle(tuple(new_tuple),self.to_grid))
        return extension_list

    def is_solved(self):
        return self.from_grid==self.to_grid




if __name__ == "__main__":
    import doctest
    doctest.testmod()
    target_grid = (("1", "2", "3"), ("4", "5", "*"))
    start_grid = (("*", "2", "3"), ("1", "4", "5"))
    from puzzle_tools import breadth_first_solve, depth_first_solve
    from time import time
    start = time()
    solution = breadth_first_solve(MNPuzzle(start_grid, target_grid))
    end = time()
    print("BFS solved: \n\n{} \n\nin {} seconds".format(
        solution, end - start))
    start = time()
    solution = depth_first_solve((MNPuzzle(start_grid, target_grid)))
    end = time()
    print("DFS solved: \n\n{} \n\nin {} seconds".format(
        solution, end - start))