"""
Some functions for working with puzzles
"""
from Queue import Queue
from puzzle import Puzzle
from collections import deque
# set higher recursion limit
# which is needed in PuzzleNode.__str__
# uncomment the next two lines on a unix platform, say CDF
# import resource
# resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))
import sys
sys.setrecursionlimit(10**6)


def depth_first_solve(puzzle):
    return depth_first_search_solve(puzzle,[])

def depth_first_search_solve(puzzle,checked):
    if puzzle in checked or puzzle.fail_fast():
        return None
    checked.append(puzzle)
    solution_path=PuzzleNode(puzzle)
    if puzzle.is_solved():
        return solution_path
    for child in puzzle.extensions():
        solution=depth_first_search_solve(child,checked)
        if solution:
            solution.parent=solution_path
            solution_path.children=[solution]
            return solution_path

def breadth_first_solve(puzzle):
    if puzzle.is_solved():
        return PuzzleNode(puzzle)
    return breadth_fist_solve_path(puzzle,[])

def breadth_fist_solve_path(puzzle,checked):
    if puzzle in checked:
        return None
    checked.append(puzzle)
    solution_path=PuzzleNode(puzzle)
    if puzzle.fail_fast():
        return None
    b=puzzle.extensions()
    if b:
        for child in b:
            if child.is_solved():
                solution=PuzzleNode(child)
                solution.parent=[solution_path]
                solution_path.children=[solution]
                return solution_path
        for child in b:
            solution=breadth_fist_solve_path(child,checked)
            if solution:
                solution.parent=solution_path
                solution_path.children=[solution]
                return solution_path

class PuzzleNode:
    """
    A Puzzle configuration that refers to other configurations that it
    can be extended to.
    """

    def __init__(self, puzzle=None, children=None, parent=None):
        """
        Create a new puzzle node self with configuration puzzle.

        @type self: PuzzleNode
        @type puzzle: Puzzle | None
        @type children: list[PuzzleNode]
        @type parent: PuzzleNode | None
        @rtype: None
        """
        self.puzzle, self.parent = puzzle, parent
        if children is None:
            self.children = []
        else:
            self.children = children[:]

    def __eq__(self, other):
        """
        Return whether PuzzleNode self is equivalent to other

        @type self: PuzzleNode
        @type other: PuzzleNode | Any
        @rtype: bool

        >>> from word_ladder_puzzle import WordLadderPuzzle
        >>> pn1 = PuzzleNode(WordLadderPuzzle("on", "no", {"on", "no", "oo"}))
        >>> pn2 = PuzzleNode(WordLadderPuzzle("on", "no", {"on", "oo", "no"}))
        >>> pn3 = PuzzleNode(WordLadderPuzzle("no", "on", {"on", "no", "oo"}))
        >>> pn1.__eq__(pn2)
        True
        >>> pn1.__eq__(pn3)
        False
        """
        return (type(self) == type(other) and
                self.puzzle == other.puzzle and
                all([x in self.children for x in other.children]) and
                all([x in other.children for x in self.children]))

    def __str__(self):
        """
        Return a human-readable string representing PuzzleNode self.

        # doctest not feasible.
        """
        return "{}\n\n{}".format(self.puzzle,
                                 "\n".join([str(x) for x in self.children]))