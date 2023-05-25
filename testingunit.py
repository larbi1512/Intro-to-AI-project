import unittest
from problem import Problem
from toolbox import *

class TestProblem(unittest.TestCase):
    # a star algorithm test unit
    def test_a_star_search(self):
         # Test case 2: Graph with loops and cycles
        problem1 = Problem([])
        problem1.graph.add_edge('A', 'B', weight=1)
        problem1.graph.add_edge('A', 'C', weight=2)
        problem1.graph.add_edge('B', 'C', weight=1)
        problem1.graph.add_edge('B', 'D', weight=5)
        problem1.graph.add_edge('C', 'D', weight=8)
        problem1.graph.add_edge('C', 'E', weight=3)
        problem1.graph.add_edge('D', 'E', weight=2)
        problem1.graph.add_edge('D', 'F', weight=4)
        problem1.graph.add_edge('E', 'F', weight=1)
        problem1.modify_heuristic_value('A', 'F', 10)
        problem1.modify_heuristic_value('B', 'F', 8)
        problem1.modify_heuristic_value('C', 'F', 6)
        problem1.modify_heuristic_value('D', 'F', 4)
        problem1.modify_heuristic_value('E', 'F', 2)
        start_node1 = 'A'
        goal_node1 = 'F'
        expected_path1 = ['A', 'C', 'E', 'F']
        t1 = toolbox(problem1)
        t1.animate_solution(problem1.a_star_search(start_node1, goal_node1))
        self.assertEqual(problem1.a_star_search(start_node1, goal_node1), expected_path1)
        
        # even more complicated test case 
        problem1 = Problem([])
        problem1.add_an_edge(("A", "B"))
        problem1.graph.add_edge('A', 'C', weight=2)
        problem1.modify_edge_weight(("A", "C"), 5)
        problem1.graph.add_edge('B', 'C', weight=1)
        problem1.graph.add_edge('B', 'D', weight=5)
        problem1.graph.add_edge('C', 'D', weight=8)
        problem1.graph.add_edge('C', 'E', weight=3)
        problem1.graph.add_edge('D', 'E', weight=2)
        problem1.graph.add_edge('D', 'F', weight=4)
        problem1.graph.add_edge('E', 'F', weight=7)
        problem1.graph.add_edge('E', 'G', weight=4)
        problem1.graph.add_edge('F', 'G', weight=3)
        problem1.modify_heuristic_value('A', 10)
        problem1.modify_heuristic_value('B', 8)
        problem1.modify_heuristic_value('C', 6)
        problem1.modify_heuristic_value('D', 4)
        problem1.modify_heuristic_value('E', 2)
        problem1.modify_heuristic_value('F', 1)
        start_node1 = 'A'
        goal_node1 = 'G'
        expected_path1 = ['A', 'C', 'E', 'F', 'G']
        t1 = toolbox(problem1)
        t1.animate_solution(problem1.a_star_search(start_node1, goal_node1))
        self.assertEqual(problem1.a_star_search(start_node1, goal_node1), expected_path1)

    def greedy_best_first_search(self):
        # Test case 2: Graph with loops and cycles
        problem1 = Problem([])
        problem1.graph.add_edge('A', 'B', weight=1)
        problem1.graph.add_edge('A', 'C', weight=2)
        problem1.graph.add_edge('B', 'C', weight=1)
        problem1.graph.add_edge('B', 'D', weight=5)
        problem1.graph.add_edge('C', 'D', weight=8)
        problem1.graph.add_edge('C', 'E', weight=3)
        problem1.graph.add_edge('D', 'E', weight=2)
        problem1.graph.add_edge('D', 'F', weight=4)
        problem1.graph.add_edge('E', 'F', weight=7)
        problem1.graph.add_edge('E', 'G', weight=4)
        problem1.graph.add_edge('F', 'G', weight=3)
        problem1.modify_heuristic_value('A', 'G', 10)
        problem1.modify_heuristic_value('B', 'G', 8)
        problem1.modify_heuristic_value('C', 'G', 6)
        problem1.modify_heuristic_value('D', 'G', 4)
        problem1.modify_heuristic_value('E', 'G', 2)
        problem1.modify_heuristic_value('F', 'G', 1)
        start_node1 = 'A'
        goal_node1 = 'G'
        expected_path1 = ['A', 'C', 'E', 'G']
        t1 = toolbox(problem1)
        t1.animate_solution(problem1.greedy_best_first_search(start_node1, goal_node1))
        self.assertEqual(problem1.greedy_best_first_search(start_node1, goal_node1), expected_path1)
        
        # test case 3 : complexe graph
        problem1 = Problem([])
        problem1.graph.add_edge('A', 'B', weight=1)
        problem1.graph.add_edge('A', 'C', weight=2)
        problem1.graph.add_edge('B', 'C', weight=1)
        problem1.graph.add_edge('B', 'D', weight=5)
        problem1.graph.add_edge('C', 'D', weight=8)
        problem1.graph.add_edge('C', 'E', weight=3)
        problem1.graph.add_edge('D', 'E', weight=2)
        problem1.graph.add_edge('D', 'F', weight=4)
        problem1.graph.add_edge('E', 'F', weight=7)
        problem1.graph.add_edge('E', 'G', weight=4)
        problem1.graph.add_edge('F', 'G', weight=3)
        problem1.modify_heuristic_value('A', 'G', 10)
        problem1.modify_heuristic_value('B', 'G', 8)
        problem1.modify_heuristic_value('C', 'G', 6)
        problem1.modify_heuristic_value('D', 'G', 4)
        problem1.modify_heuristic_value('E', 'G', 2)
        problem1.modify_heuristic_value('F', 'G', 1)
        start_node1 = 'A'
        goal_node1 = 'G'
        expected_path1 = ['A', 'C', 'E', 'G']
        t1 = toolbox(problem1)
        t1.animate_solution(problem1.greedy_best_first_search(start_node1, goal_node1))
        self.assertEqual(problem1.greedy_best_first_search(start_node1, goal_node1), expected_path1)
     
        
class TestHillClimbing(unittest.TestCase):
    def test_hill_climbing_search(self):
        # Test case 1: Basic functionality on a simple graph
        print("test case 1")
        problem1 = Problem([])
        problem1.initial_state = 'A'
        problem1.add_goal_state('C')
        problem1.add_an_edge(('A', 'B'), 4)
        problem1.add_an_edge(('A', 'C'), 2)
        problem1.add_an_edge(('B', 'C'), 1)
        problem1.add_an_edge(('B', 'D'), 5)
        problem1.add_an_edge(('C', 'D'), 8)
        problem1.modify_heuristic_value('A',  7)
        problem1.modify_heuristic_value('B',  6)
        problem1.modify_heuristic_value('C',  3)
        problem1.modify_heuristic_value('D',  0)
        goal_node1 = 'C'
        self.assertEqual(problem1.hill_climbing(), goal_node1)
        t = toolbox(problem1)
        t.animate_solution(problem1.hill_climbing())

        # Test case 2: Graph with loops and cycles
        print("test case 2")
        problem2 = Problem([])
        problem2.initial_state = 'A'
        problem2.add_goal_state('C')
        problem2.add_an_edge(('A', 'B'), 2)
        problem2.add_an_edge(('B', 'C'), 3)
        problem2.add_an_edge(('C', 'D'), 4)
        problem2.add_an_edge(('D', 'A'), 5)
        problem2.add_an_edge(('B', 'D'), 1)
        problem2.modify_heuristic_value('A',  7)
        problem2.modify_heuristic_value('B',  6)
        problem2.modify_heuristic_value('D',  3)
        problem2.modify_heuristic_value('C',  0)
        goal_node2 = 'C'
        self.assertEqual(problem2.hill_climbing(), goal_node2)
        t2 = toolbox(problem2)
        t2.animate_solution(problem2.hill_climbing())
        
        # Test case 3: Graph with multiple goal nodes
        print("test case 3")
        problem4 = Problem([])
        problem4.initial_state = 'A'
        problem4.add_goal_state('E')
        problem4.add_an_edge(('A', 'B'), 4)
        problem4.add_an_edge(('A', 'C'), 2)
        problem4.add_an_edge(('B', 'C'), 1)
        problem4.add_an_edge(('B', 'D'), 5)
        problem4.add_an_edge(('C', 'D'), 8)
        problem4.add_an_edge(('C', 'E'), 3)
        problem4.add_an_edge(('D', 'E'), 6)
        problem4.modify_heuristic_value('A',  10)
        problem4.modify_heuristic_value('B',  8)
        problem4.modify_heuristic_value('C',  4)
        start_node4 = 'A'
        goal_node4 = 'E'
        self.assertEqual(problem4.hill_climbing(), goal_node4)
        t4 = toolbox(problem4)
        t4.animate_solution(problem4.hill_climbing())

if __name__ == '__main__':
    unittest.main()
        
test = TestHillClimbing()
test.test_hill_climbing_search()        
        