from TestRunner import TestRunner
from scipy.optimize import minimize
import numpy as np

test_runner = TestRunner()

test_runner.run()
test_runner.draw_plot()
score = test_runner.get_score()

print("score: {}".format(score))

x0 = np.array([1,1,1])

def controller_score(K):
    Kp,Ki,Kd = K
    test_runner = TestRunner()
    test_runner.vehicle_controller.controller.Kp = Kp
    test_runner.vehicle_controller.controller.Ki = Ki
    test_runner.vehicle_controller.controller.Kd = Kd
    
    test_runner.run()
    score = test_runner.get_score()
    return score

bounds = [(0,np.inf),(0,np.inf),(0,np.inf)]
res = minimize(controller_score,x0, method='SLSQP', bounds=bounds)
print(res)