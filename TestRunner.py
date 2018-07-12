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

    def _controller_score(self,parameters):
        self.vehicle_controller.set_control_parameters(parameters)
        self.run()
        return self.get_score()

    def optimise(self):
        parameters = self.vehicle_controller.get_control_parameters()
        bounds = self.vehicle_controller.get_control_parameter_bounds()
        print("optimising control parameters. This will take a while. Unless you don't have cython installed, in which case it will take an age.\n")
        
        print("results:\n")
        result = minimize(self._controller_score,parameters, method='SLSQP', bounds=bounds)
        print(result)

    def run(self):
        self.vehicle_controller.set_timestep(self.timestep)
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