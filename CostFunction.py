import numpy as np

def simple_cost_function(results):
    return sum(np.square(results.error))