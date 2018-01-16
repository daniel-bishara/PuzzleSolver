from puzzle import Puzzle


class WordLadderPuzzle(Puzzle):
    """
    A word-ladder puzzle that may be solved, unsolved, or even unsolvable.
    """

    def __init__(self, from_word, to_word, ws):
        """
        Create a new word-ladder puzzle with the aim of stepping
        from from_word to to_word using words in ws, changing one
        character at each step.

        @type from_word: str
        @type to_word: str
        @type ws: set[str]
        @rtype: None
        """
        (self._from_word, self._to_word, self._word_set) = (from_word,
                                                            to_word, ws)
        # set of characters to use for 1-character changes
        self._chars = "abcdefghijklmnopqrstuvwxyz"

    # TODO
    # implement __eq__ and __str__
    # __repr__ is up to you
    def __eq__(self, other):
        '''
        Return whether WordLadder self is equal to other

        @type self: WordLadderPuzzle
        @type other: WordLadderPuzzle
        @rtype: bool

        >>> word_set = set(['dog','cat','lion'])
        >>> w1 = WordLadderPuzzle('mom','dad',word_set)
        >>> w2 = WordLadderPuzzle('mom','dad',word_set)
        >>> w1 == w2
        True
        >>> w3 = WordLadderPuzzle('cat','mom',word_set)
        >>> w1 == w3
        False

        '''
        return self._from_word == other._from_word and self._to_word == other._to_word

    def __str__(self):
        '''
        Return a human-readable string representation of WordLadderPuzzle self

        @rtype: str
        '''
        return "{} --> {}".format(self._from_word,self._to_word)

    # TODO
    # override extensions
    # legal extensions are WordLadderPuzzles that have a from_word that can
    # be reached from this one by changing a single letter to one of those
    # in self._chars
    def extensions(self):
        '''
        Return list of extensions of WordLadder Puzzle

        @type self: WordLadderPuzzle
        @rtype: list[WordLadderPuzzle]

        >>> file = open("words.txt", "r")
        >>> word_set = set(file.read().split())
        >>> file.close()
        >>> exten_list = ['bog', 'cog', 'dog', 'fog', 'Gog', 'hog', 'jog', 'log', 'tog']
        >>> exten_list += ['dig', 'dog', 'dug', 'doc', 'doe', 'dog', 'don', 'dos', 'dot', 'Dow']
        >>> w1 = WordLadderPuzzle('dog','god',word_set)
        >>> L1 = w1.extensions()
        >>> L2 = [x._from_word for x in L1]
        >>> len(L2) == len(exten_list)
        True
        >>> all([w in exten_list for w in L2])
        True
        >>> all([w in L2 for w in exten_list])
        True

        '''

        #convinient names
        chars, to_word , word_set = self._chars, self._to_word, self._word_set
        from_word = self._from_word

        reduced_word_set = self.get_reduced_word_set()
        extensions = []

        for i in range(len(from_word)):
            for chr in chars:
                new_from = from_word.replace(from_word[i],chr)
                if new_from != from_word or new_from.capitalize() != from_word:
                    if new_from in reduced_word_set:
                        extensions.append(WordLadderPuzzle(new_from,to_word,word_set))

                    elif new_from.capitalize() in reduced_word_set:
                        extensions.append(WordLadderPuzzle(new_from.capitalize(),to_word,word_set))

        return extensions

    def get_reduced_word_set(self):
        '''
        Return a list of words from self's word_set which have the same length as self's from_word

        @type self: WordLadderPuzzle
        @rtype: list[str]
        '''

        #convinient names
        word_length, word_set,to_word = len(self._from_word), self._word_set,self._to_word

        return [x for x in word_set if len(x) == word_length ]

    # TODO
    # override is_solved
    # this WordLadderPuzzle is solved when _from_word is the same as
    # _to_word
    def is_solved(self):
        '''
        Return whether WordLadderPuzzle self is solved

        @type self: WordLadderPuzzle
        @rtype: bool

        >>> file = open("words.txt", "r")
        >>> word_set = set(file.read().split())
        >>> file.close()
        >>> w1 = WordLadderPuzzle('dog','god',word_set)
        >>> w1.is_solved()
        False
        >>> w2 = WordLadderPuzzle('dog','dog',word_set)
        >>> w2.is_solved()
        True
        '''
        return self._from_word == self._to_word


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    from puzzle_tools import breadth_first_solve, depth_first_solve
    from time import time
    with open("words.txt", "r") as words:
        word_set = set(words.read().split())
    w = WordLadderPuzzle("same", "cost", word_set)
    start = time()
    sol = breadth_first_solve(w)
    end = time()
    print("Solving word ladder from same->cost")
    print("...using breadth-first-search")
    print("Solutions: {} took {} seconds.".format(sol, end - start))
    start = time()
    sol = depth_first_solve(w)
    end = time()
    print("Solving word ladder from same->cost")
    print("...using depth-first-search")
    print("Solutions: {} took {} seconds.".format(sol, end - start))