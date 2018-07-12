from VehicleController import VehicleController
from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import minimize
from ObstacleCourse import ObstacleCourse
from CostFunction import simple_cost_function

class Results:
    def __init__(self):
        self.positions = []
        self.setpoint = []
        self.error = []
        
class TestRunner:
    def __init__(self,controller=VehicleController(),cost_function=simple_cost_function):
        self.current_time = 0.0
        self.timestep = 0.2
        self.max_time = 100
        self.vehicle_controller = controller
        self.pilot = ObstacleCourse()
        self.cost_function = cost_function
        self.results = Results()

    def _objective_function(self,parameters):
        test_runner=TestRunner()
        test_runner.set_control_parameters(parameters)
        test_runner.run()
        score = test_runner.get_score()
        return score

    def optimise(self,update_on_failure=True,maxiter=1000):
        self.run()
        intial_score = self.get_score()

        initial_parameters = self.get_control_parameters()
        bounds = self.vehicle_controller.get_control_parameter_bounds()
        constraints = {'type':'ineq', 'fun': lambda x: x}
        options={}
        options['maxiter']=maxiter
        print("optimising control parameters. This will take a while, unless it takes longer.\n")
        
        result = minimize(self._objective_function,initial_parameters, method='COBYLA', constraints=constraints, options=options) # this method is slow, and produces a worse result, but it works every time
        #result = minimize(self._objective_function,initial_parameters, method='SLSQP', bounds=bounds) # this method seems to work sporadically. when it does work, it's faster and more optimal
        
        if result.success:
            print("optimisation terminated successfully\n")
        else:
            print("optimisation failed: {}\n".format(result.message))
            if update_on_failure:
                print("using last value") 
            else:
                return

        optimal_parameters = result.x
        self.set_control_parameters(optimal_parameters)
        self.run()
        optimal_score = self.get_score()

        if verbose:
            print(result)

        print()
        print("initial parameters:\n\tcontrol parameters: {}\n\tscore: {}\n".format(initial_parameters, intial_score))
        print("optimal parameters:\n\tcontrol parameters: {}\n\tscore: {}\n".format(optimal_parameters, optimal_score))

        return result


    def reset(self):
        self.results.positions.clear()
        self.results.setpoint.clear()
        self.results.error.clear()

        self.current_time=0

        self.vehicle_controller.set_timestep(self.timestep)
        self.vehicle_controller.vehicle_model.position = 0 #TODO this is bad encapsulation
        

    def run(self):
        self.reset()

        self.vehicle_controller.set_setpoint(self.pilot.get_setpoint(self.current_time))

        self.results.positions.append(self.vehicle_controller.get_position())
        self.results.setpoint.append(self.vehicle_controller.setpoint)
        self.results.error.append(self.vehicle_controller.error)

        while self.current_time < self.max_time:
            self.vehicle_controller.set_setpoint(self.pilot.get_setpoint(self.current_time))
            self.vehicle_controller.run_step()
            self.results.positions.append(self.vehicle_controller.get_position())
            self.results.setpoint.append(self.vehicle_controller.setpoint)
            self.results.error.append(self.vehicle_controller.error)
            self.current_time += self.timestep
        
    def draw_plot(self):
        ymax = max( max( self.results.positions), max(self.results.setpoint), max(self.results.error) )
        ymin = min( min( self.results.positions), min(self.results.setpoint), min(self.results.error) )
        
        plt.plot(self.results.positions)
        plt.plot(self.results.setpoint)
        plt.plot(self.results.error)
        plt.ylim(ymin,ymax)
        plt.legend(["position","setpoint","error"])
        plt.show()
        
    def get_score(self):
        return self.cost_function(self.results)

    def get_control_parameters(self):
        return self.vehicle_controller.get_control_parameters()

    def get_control_parameter_bounds(self):
        return self.vehicle_controller.get_control_parameter_bounds()

    def set_control_parameters(self,parameters):
        self.vehicle_controller.set_control_parameters(parameters)