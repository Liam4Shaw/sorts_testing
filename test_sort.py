import unittest 
from sort import selection_sort, bubble_sort, insertion_sort

class TestSort(unittest.TestCase):

    test_cases = [
        # Different integer cases
        ([5, 1, 9, 0, 5], [0, 1, 5, 5, 9]),
        ([1], [1]),
        ([1, 1, 0, 0, 1, 0], [0, 0, 0, 1, 1, 1]),
        ([1, 2, 4, 5], [1, 2, 4, 5]),
        ([9, 7, 5, 4, 1, 0], [0, 1, 4, 5, 7, 9]),
        # Empty list case
        ([], []),
        # Negative integer case
        ([0, -5, -1, 99, 7, 6, 0, -99], [-99, -5, -1, 0, 0, 6, 7, 99]),
        # float case
        ([115.15, 215, 113, 215.00, 925, 215.0, 115.150, 115.05, 81, 115.16, 115.14, 115.145], [81, 113, 115.05, 115.14, 115.145, 115.15, 115.15, 115.16, 215, 215, 215, 925]),
        # String comparisons (lexographical order)
        # Commonly used character ascii values: 0-9 -> 48-57; A-Z -> 65-90; a-z -> 97-122; space(' ') -> 32; NULL('') -> 0
        (['bac', 'abc'], ['abc', 'bac']),
        (['animal', 'Animal', 'Zebra', 'Horse', 'aan', 'an'], ['Animal', 'Horse', 'Zebra', 'aan', 'an', 'animal']),
        (['a0', '0a', 'a', 'A', '1a', '11a', '', ' a', 'a01', 'aa', ' ', 'a ', 'a'], ['', ' ', ' a', '0a', '11a', '1a', 'A', 'a', 'a', 'a ', 'a0', 'a01', 'aa'])
    ]

    TypeError_test_cases = [
        [1, 'green', 3],
        # During iteration through the main list, while comparing an int/float/string with the nested list, the type error will rise
        [10, [2, 15]]
    ]
    
    def setUp(self): 
        # Random order list
        self.a = [3, 2.01, 4.5, 0]
        # Sorted list
        self.b = [-500, 1.1, 100, 350]
        # Descending order list
        self.c = [21, 15, 6, 0]

    def test_selection_sort(self):
        for test, ans in self.test_cases:
            self.assertEqual(selection_sort(test), ans)
        for test in self.TypeError_test_cases:
            with self.assertRaises(TypeError):
                selection_sort(test)
        
    # To compare the list at each iteration (when a swap takes place) of the selection sort algorithm 
    # (to determine whether it is indeed selection sort being implemented)
    def test_selection_sort_stages(self):
        a_stages = [
            [3, 2.01, 4.5, 0], 
            [0, 2.01, 4.5, 3], 
            [0, 2.01, 4.5, 3], 
            [0, 2.01, 3, 4.5]
        ]
        self.assertEqual(selection_sort(self.a, True), a_stages)

        b_stages = [
            [-500, 1.1, 100, 350],
            [-500, 1.1, 100, 350],
            [-500, 1.1, 100, 350],
            [-500, 1.1, 100, 350]
        ]
        self.assertEqual(selection_sort(self.b, True), b_stages)

        c_stages = [
            [21, 15, 6, 0],
            [0, 15, 6, 21],
            [0, 6, 15, 21],
            [0, 6, 15, 21]
        ]
        self.assertEqual(selection_sort(self.c, True), c_stages)


    def test_bubble_sort(self):
        for test, ans in self.test_cases:
            self.assertEqual(bubble_sort(test), ans)
        for test in self.TypeError_test_cases:
            with self.assertRaises(TypeError):
                bubble_sort(test)

    def test_bubble_sort_stages(self):
        a_stages = [
            [3, 2.01, 4.5, 0],
            [2.01, 3, 4.5, 0], [2.01, 3, 0, 4.5],
            [2.01, 0, 3, 4.5],
            [0, 2.01, 3, 4.5]
        ]
        self.assertEqual(bubble_sort(self.a, True), a_stages)
    
        b_stages = [
            [-500, 1.1, 100, 350]    
        ]    # No swaps take place
        self.assertEqual(bubble_sort(self.b, True), b_stages)

        c_stages = [
            [21, 15, 6, 0],
            [15, 21, 6, 0], [15, 6, 21, 0], [15, 6, 0, 21],
            [6, 15, 0, 21], [6, 0, 15, 21],
            [0, 6, 15, 21]
        ]
        self.assertEqual(bubble_sort(self.c, True), c_stages)


    def test_insertion_sort(self):
        for test, ans in self.test_cases:
            self.assertEqual(insertion_sort(test), ans)
        for test in self.TypeError_test_cases:
            with self.assertRaises(TypeError):
                insertion_sort(test)

    def test_insertion_sort_stages(self):
        a_stages = [
            [3, 2.01, 4.5, 0],
            [3, 3, 4.5, 0], [2.01, 3, 4.5, 0],                                                 # while key = 3
            [2.01, 3, 4.5, 0],                                                                 # while key = 4.5
            [2.01, 3, 4.5, 4.5], [2.01, 3, 3, 4.5], [2.01, 2.01, 3, 4.5], [0, 2.01, 3, 4.5]    # while key = 0  
        ]
        self.assertEqual(insertion_sort(self.a, True), a_stages)

        b_stages = [
            [-500, 1.1, 100, 350],
            [-500, 1.1, 100, 350],    # while key = 1.1
            [-500, 1.1, 100, 350],    # while key = 100
            [-500, 1.1, 100, 350]     # while key = 350
        ]
        self.assertEqual(insertion_sort(self.b, True), b_stages)

        c_stages = [
            [21, 15, 6, 0],
            [21, 21, 6, 0], [15, 21, 6, 0],                                     # while key = 15
            [15, 21, 21, 0], [15, 15, 21, 0], [6, 15, 21, 0],                   # while key = 6
            [6, 15, 21, 21], [6, 15, 15, 21], [6, 6, 15, 21], [0, 6, 15, 21]    # while key = 0
        ]
        self.assertEqual(insertion_sort(self.c, True), c_stages)


if __name__ == '__main__':
    unittest.main()