from TestRunner import TestRunner
from scipy.optimize import minimize
import numpy as np
from HighScores import HighScores

test_runner = TestRunner()
result = test_runner.optimise(verbose=True)
score = test_runner.get_score()

high_scores=HighScores()
high_scores.load()
high_scores.insert(test_runner,result,score)

test_runner.draw_plot()