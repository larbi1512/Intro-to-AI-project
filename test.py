from toolbox import *

problem = Problem([("A", "B"), ("B", "C"), ("C", "A"), ("3", "5"),
                  ("C", "G"), ("C", "M"), ("N", "A"), ("V", "5"), ("5", "C")])

t = toolbox(problem)
t.animate_solution(problem.iterative_deepening_depth_first_search("A", "5", 5))
