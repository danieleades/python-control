from TestRunner import TestRunner
from scipy.optimize import minimize
import numpy as np
from HighScores import HighScores
from MyDict import MyDict

test_runner = TestRunner()
result = test_runner.optimise(verbose=True)
score = test_runner.get_score()
hash = test_runner.get_test_hash()
parameters = test_runner.get_control_parameters()

high_scores=HighScores()
high_scores.load()
high_scores.insert(hash,parameters,score)
high_scores.save()

test_runner.draw_plot()