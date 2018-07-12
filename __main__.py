from TestRunner import TestRunner
from scipy.optimize import minimize
import numpy as np

test_runner = TestRunner()
test_runner.optimise(maxiter=2000)
test_runner.draw_plot()