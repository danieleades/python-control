from IntegralWindow import IntegralWindow
import numpy as np

class PidLoop:
    def __init__(self):
        self.Kp = 1.9
        self.Ki = 0.2
        self.Kd = 7
        self.timestep = 0
        self.error = 0
        self.last_error = 0
        self.output = 0
        self.integral_window = IntegralWindow()

    def set_error(self,error):
        self.last_error = self.error
        self.error = error
        
    def set_timestep(self,timestep):
        self.timestep = timestep

    def run_loop(self):
        self.integral_window.push_data(self.error,self.timestep)
        proportional = self.Kp*self.error
        integral = self.Ki*self.integral_window.accumulated_total
        derivative = self.Kd*(self.error - self.last_error)/self.timestep
        self.output = proportional + integral + derivative
        return self.output

    def get_control_parameters(self):
        parameters=[]
        parameters.append(self.Kp)
        parameters.append(self.Ki)
        parameters.append(self.Kd)
        return parameters
    
    def set_control_parameters(self,parameters):
        self.Kp,self.Ki,self.Kd = parameters

    def get_control_parameter_bounds(self):
        return [(0,np.inf),(0,np.inf),(0,np.inf)]