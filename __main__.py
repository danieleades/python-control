from TestRunner import TestRunner
from scipy.optimize import minimize
import numpy as np

test_runner = TestRunner()

test_runner.run()
#test_runner.draw_plot()
score = test_runner.get_score()

print("score: {}".format(score))

#x0 = np.array([1,1,1])

x0 = test_runner.get_control_parameters()

def controller_score(K):
    test_runner = TestRunner()
    test_runner.set_control_parameters(K)
    
    test_runner.run()
    score = test_runner.get_score()
    return score

bounds = [(0,np.inf),(0,np.inf),(0,np.inf)]
constraints = {'type':'ineq', 'fun': lambda x: x}
res = minimize(controller_score,x0, method='COBYLA', constraints=constraints)
optimal_parameters = res.x
print(optimal_parameters)
print(res)

test_runner.set_control_parameters(optimal_parameters)
test_runner.run()
score = test_runner.get_score()


print("score: {}".format(score))

test_runner.draw_plot()