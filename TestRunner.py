from VehicleController import VehicleController
from matplotlib import pyplot as plt
import numpy as np
from ObstacleCourse import ObstacleCourse


    
class Results:
    def __init__(self):
        self.positions = []
        self.setpoint = []
        self.error = []
        
def CostFunction(results):
    return sum(np.square(results.error))

class TestRunner:
    def __init__(self):
        self.current_time = 0.0
        self.timestep = 0.2
        self.max_time = 100
        self.vehicle_controller = VehicleController()
        self.pilot = ObstacleCourse()
        self.cost_function = CostFunction
        self.results = Results()
        
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
        
        plot = plt.plot(self.results.positions)
        plot = plt.plot(self.results.setpoint)
        plot = plt.plot(self.results.error)
        plt.ylim(ymin,ymax)
        plt.legend(["position","setpoint","error"])
        plt.show()
        
    def get_score(self):
        
        return self.cost_function(self.results)