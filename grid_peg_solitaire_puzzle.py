from puzzle import Puzzle


class GridPegSolitairePuzzle(Puzzle):
    """
    Snapshot of peg solitaire on a rectangular grid. May be solved,
    unsolved, or even unsolvable.
    """

    def __init__(self, marker, marker_set):
        """
        Create a new GridPegSolitairePuzzle self with
        marker indicating pegs, spaces, and unused
        and marker_set indicating allowed markers.

        @type marker: list[list[str]]
        @type marker_set: set[str]
                          "#" for unused, "*" for peg, "." for empty
        """
        assert isinstance(marker, list)
        assert len(marker) > 0
        assert all([len(x) == len(marker[0]) for x in marker[1:]])
        assert all([all(x in marker_set for x in row) for row in marker])
        assert all([x == "*" or x == "." or x == "#" for x in marker_set])
        self._marker, self._marker_set = marker, marker_set

    def is_solved(self):
        count=0
        for row in self._marker:
            for element in row:
                if element == "*":
                    count+=1
        return count==1

    def __eq__(self, other):
        '''
        Return whether GridPegSolitairePuzzle self is equivalent to other.

        @type self: GridPegSolitairePuzzle
        @type other: GridPegSolitairePuzzle | Any
        @rtype: bool

        >>> grid = [["*", "*", "*", "*", "*"], ["*", "*", "*", "*", "*"], ["*", "*", "*", "*", "*"]]
        >>> g1 = GridPegSolitairePuzzle(grid,{"*", ".", "#"})
        >>> g2 = GridPegSolitairePuzzle(grid,{"*", ".", "#"})
        >>> g1 == g2
        True
        >>> grid2 = [["#", "*", "*", "*", "*"], ["#", "*", "*", "*", "*"],["#", "*", "*", "*", "*"]]
        >>> g3 = GridPegSolitairePuzzle(grid2,{"*", ".", "#"})
        >>> g1 == g3
        False

        '''
        return self._marker==other._marker and self._marker_set==other._marker_set


    def __str__(self):
        string_representation=""
        for row in self._marker:
            for element in row:
                string_representation+=(str(element)+" ")
            string_representation+="\n"
        return string_representation

    def extensions (self):
        empty_spaces=[]
        extension_list=[]
        for y in range (len(self._marker)):
            for x in range (len(self._marker[0])):
                if self._marker[y][x]==".":
                    empty_spaces.append([x,y])
        for empty_space in empty_spaces:
            x,y=empty_space[0],empty_space[1]
            if x-2>=0:
                if self._marker[y][x-2]=="*" and self._marker[y][x-1]=="*":
                    new_list=copy_nested_list(self._marker)
                    new_list[y][x],new_list[y][x-2],new_list[y][x-1]="*",".","."
                    extension_list.append(GridPegSolitairePuzzle(new_list,self._marker_set))
            if x+3<=len(self._marker[0]):
                if self._marker[y][x+2]=="*" and self._marker[y][x+1]=="*":
                    new_list=copy_nested_list(self._marker)
                    new_list[y][x],new_list[y][x+2],new_list[y][x+1]="*",".","."
                    extension_list.append(GridPegSolitairePuzzle(new_list,self._marker_set))
            if y-2>=0:
                if self._marker[y-2][x]=="*" and self._marker[y-1][x]=="*":
                    new_list=copy_nested_list(self._marker)
                    new_list[y][x],new_list[y-2][x],new_list[y-1][x]="*",".","."
                    extension_list.append(GridPegSolitairePuzzle(new_list,self._marker_set))
            if y+3<=len(self._marker[0]):
                if self._marker[y+2][x]=="*" and self._marker[y+1][x]=="*":
                    new_list=copy_nested_list(self._marker)
                    new_list[y][x],new_list[y+2][x],new_list[y+1][x]="*",".","."
                    extension_list.append(GridPegSolitairePuzzle(new_list,self._marker_set))
        return extension_list

def copy_nested_list(marker):
    new_list=[]
    for row in marker:
        new_list.append(row[:])
    return new_list

if __name__ == "__main__":
    import doctest

    doctest.testmod()
    from puzzle_tools import depth_first_solve

    grid = [["*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*"],
            ["*", "*", ".", "*", "*"],
            ["*", "*", "*", "*", "*"]]
    gpsp = GridPegSolitairePuzzle(grid, {"*", ".", "#"})
    import time

    start = time.time()
    solution = depth_first_solve(gpsp)
    end = time.time()
    print("Solved 5x5 peg solitaire in {} seconds.".format(end - start))
    print("Using depth-first: \n{}".format(solution))